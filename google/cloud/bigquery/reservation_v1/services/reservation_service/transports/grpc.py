# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from typing import Callable, Dict, Tuple

from google.api_core import grpc_helpers  # type: ignore
from google.auth import credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore


import grpc  # type: ignore

from google.cloud.bigquery.reservation_v1.types import reservation
from google.cloud.bigquery.reservation_v1.types import reservation as gcbr_reservation
from google.protobuf import empty_pb2 as empty  # type: ignore

from .base import ReservationServiceTransport


class ReservationServiceGrpcTransport(ReservationServiceTransport):
    """gRPC backend transport for ReservationService.

    This API allows users to manage their flat-rate BigQuery
    reservations.

    A reservation provides computational resource guarantees, in the
    form of `slots <https://cloud.google.com/bigquery/docs/slots>`__, to
    users. A slot is a unit of computational power in BigQuery, and
    serves as the basic unit of parallelism. In a scan of a
    multi-partitioned table, a single slot operates on a single
    partition of the table. A reservation resource exists as a child
    resource of the admin project and location, e.g.:
    projects/myproject/locations/US/reservations/reservationName.

    A capacity commitment is a way to purchase compute capacity for
    BigQuery jobs (in the form of slots) with some committed period of
    usage. A capacity commitment resource exists as a child resource of
    the admin project and location, e.g.:
    projects/myproject/locations/US/capacityCommitments/id.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    def __init__(
        self,
        *,
        host: str = "bigqueryreservation.googleapis.com",
        credentials: credentials.Credentials = None,
        channel: grpc.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): The mutual TLS endpoint. If
                provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]): A
                callback to provide client SSL certificate bytes and private key
                bytes, both in PEM format. It is ignored if ``api_mtls_endpoint``
                is None.

        Raises:
          google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
        """
        if channel:
            # Sanity check: Ensure that channel and credentials are not both
            # provided.
            credentials = False

            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
        elif api_mtls_endpoint:
            host = (
                api_mtls_endpoint
                if ":" in api_mtls_endpoint
                else api_mtls_endpoint + ":443"
            )

            # Create SSL credentials with client_cert_source or application
            # default SSL credentials.
            if client_cert_source:
                cert, key = client_cert_source()
                ssl_credentials = grpc.ssl_channel_credentials(
                    certificate_chain=cert, private_key=key
                )
            else:
                ssl_credentials = SslCredentials().ssl_credentials

            # create a new channel. The provided one is ignored.
            self._grpc_channel = grpc_helpers.create_channel(
                host,
                credentials=credentials,
                ssl_credentials=ssl_credentials,
                scopes=self.AUTH_SCOPES,
            )

        # Run the base constructor.
        super().__init__(host=host, credentials=credentials)
        self._stubs = {}  # type: Dict[str, Callable]

    @classmethod
    def create_channel(
        cls,
        host: str = "bigqueryreservation.googleapis.com",
        credentials: credentials.Credentials = None,
        **kwargs
    ) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            address (Optionsl[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return grpc_helpers.create_channel(
            host, credentials=credentials, scopes=cls.AUTH_SCOPES, **kwargs
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Sanity check: Only create a new channel if we do not already
        # have one.
        if not hasattr(self, "_grpc_channel"):
            self._grpc_channel = self.create_channel(
                self._host, credentials=self._credentials
            )

        # Return the channel from cache.
        return self._grpc_channel

    @property
    def create_reservation(
        self
    ) -> Callable[
        [gcbr_reservation.CreateReservationRequest], gcbr_reservation.Reservation
    ]:
        r"""Return a callable for the create reservation method over gRPC.

        Creates a new reservation resource.

        Returns:
            Callable[[~.CreateReservationRequest],
                    ~.Reservation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_reservation" not in self._stubs:
            self._stubs["create_reservation"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/CreateReservation",
                request_serializer=gcbr_reservation.CreateReservationRequest.serialize,
                response_deserializer=gcbr_reservation.Reservation.deserialize,
            )
        return self._stubs["create_reservation"]

    @property
    def list_reservations(
        self
    ) -> Callable[
        [reservation.ListReservationsRequest], reservation.ListReservationsResponse
    ]:
        r"""Return a callable for the list reservations method over gRPC.

        Lists all the reservations for the project in the
        specified location.

        Returns:
            Callable[[~.ListReservationsRequest],
                    ~.ListReservationsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_reservations" not in self._stubs:
            self._stubs["list_reservations"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/ListReservations",
                request_serializer=reservation.ListReservationsRequest.serialize,
                response_deserializer=reservation.ListReservationsResponse.deserialize,
            )
        return self._stubs["list_reservations"]

    @property
    def get_reservation(
        self
    ) -> Callable[[reservation.GetReservationRequest], reservation.Reservation]:
        r"""Return a callable for the get reservation method over gRPC.

        Returns information about the reservation.

        Returns:
            Callable[[~.GetReservationRequest],
                    ~.Reservation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_reservation" not in self._stubs:
            self._stubs["get_reservation"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/GetReservation",
                request_serializer=reservation.GetReservationRequest.serialize,
                response_deserializer=reservation.Reservation.deserialize,
            )
        return self._stubs["get_reservation"]

    @property
    def delete_reservation(
        self
    ) -> Callable[[reservation.DeleteReservationRequest], empty.Empty]:
        r"""Return a callable for the delete reservation method over gRPC.

        Deletes a reservation. Returns
        ``google.rpc.Code.FAILED_PRECONDITION`` when reservation has
        assignments.

        Returns:
            Callable[[~.DeleteReservationRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_reservation" not in self._stubs:
            self._stubs["delete_reservation"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/DeleteReservation",
                request_serializer=reservation.DeleteReservationRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["delete_reservation"]

    @property
    def update_reservation(
        self
    ) -> Callable[
        [gcbr_reservation.UpdateReservationRequest], gcbr_reservation.Reservation
    ]:
        r"""Return a callable for the update reservation method over gRPC.

        Updates an existing reservation resource.

        Returns:
            Callable[[~.UpdateReservationRequest],
                    ~.Reservation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_reservation" not in self._stubs:
            self._stubs["update_reservation"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/UpdateReservation",
                request_serializer=gcbr_reservation.UpdateReservationRequest.serialize,
                response_deserializer=gcbr_reservation.Reservation.deserialize,
            )
        return self._stubs["update_reservation"]

    @property
    def create_capacity_commitment(
        self
    ) -> Callable[
        [reservation.CreateCapacityCommitmentRequest], reservation.CapacityCommitment
    ]:
        r"""Return a callable for the create capacity commitment method over gRPC.

        Creates a new capacity commitment resource.

        Returns:
            Callable[[~.CreateCapacityCommitmentRequest],
                    ~.CapacityCommitment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_capacity_commitment" not in self._stubs:
            self._stubs["create_capacity_commitment"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/CreateCapacityCommitment",
                request_serializer=reservation.CreateCapacityCommitmentRequest.serialize,
                response_deserializer=reservation.CapacityCommitment.deserialize,
            )
        return self._stubs["create_capacity_commitment"]

    @property
    def list_capacity_commitments(
        self
    ) -> Callable[
        [reservation.ListCapacityCommitmentsRequest],
        reservation.ListCapacityCommitmentsResponse,
    ]:
        r"""Return a callable for the list capacity commitments method over gRPC.

        Lists all the capacity commitments for the admin
        project.

        Returns:
            Callable[[~.ListCapacityCommitmentsRequest],
                    ~.ListCapacityCommitmentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_capacity_commitments" not in self._stubs:
            self._stubs["list_capacity_commitments"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/ListCapacityCommitments",
                request_serializer=reservation.ListCapacityCommitmentsRequest.serialize,
                response_deserializer=reservation.ListCapacityCommitmentsResponse.deserialize,
            )
        return self._stubs["list_capacity_commitments"]

    @property
    def get_capacity_commitment(
        self
    ) -> Callable[
        [reservation.GetCapacityCommitmentRequest], reservation.CapacityCommitment
    ]:
        r"""Return a callable for the get capacity commitment method over gRPC.

        Returns information about the capacity commitment.

        Returns:
            Callable[[~.GetCapacityCommitmentRequest],
                    ~.CapacityCommitment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_capacity_commitment" not in self._stubs:
            self._stubs["get_capacity_commitment"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/GetCapacityCommitment",
                request_serializer=reservation.GetCapacityCommitmentRequest.serialize,
                response_deserializer=reservation.CapacityCommitment.deserialize,
            )
        return self._stubs["get_capacity_commitment"]

    @property
    def delete_capacity_commitment(
        self
    ) -> Callable[[reservation.DeleteCapacityCommitmentRequest], empty.Empty]:
        r"""Return a callable for the delete capacity commitment method over gRPC.

        Deletes a capacity commitment. Attempting to delete capacity
        commitment before its commitment_end_time will fail with the
        error code ``google.rpc.Code.FAILED_PRECONDITION``.

        Returns:
            Callable[[~.DeleteCapacityCommitmentRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_capacity_commitment" not in self._stubs:
            self._stubs["delete_capacity_commitment"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/DeleteCapacityCommitment",
                request_serializer=reservation.DeleteCapacityCommitmentRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["delete_capacity_commitment"]

    @property
    def update_capacity_commitment(
        self
    ) -> Callable[
        [reservation.UpdateCapacityCommitmentRequest], reservation.CapacityCommitment
    ]:
        r"""Return a callable for the update capacity commitment method over gRPC.

        Updates an existing capacity commitment.

        Only plan and renewal_plan fields can be updated. Plan can only
        be changed to a plan of a longer commitment period. Attempting
        to change to a plan with shorter commitment period will fail
        with the error code ``google.rpc.Code.FAILED_PRECONDITION``.

        Returns:
            Callable[[~.UpdateCapacityCommitmentRequest],
                    ~.CapacityCommitment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_capacity_commitment" not in self._stubs:
            self._stubs["update_capacity_commitment"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/UpdateCapacityCommitment",
                request_serializer=reservation.UpdateCapacityCommitmentRequest.serialize,
                response_deserializer=reservation.CapacityCommitment.deserialize,
            )
        return self._stubs["update_capacity_commitment"]

    @property
    def split_capacity_commitment(
        self
    ) -> Callable[
        [reservation.SplitCapacityCommitmentRequest],
        reservation.SplitCapacityCommitmentResponse,
    ]:
        r"""Return a callable for the split capacity commitment method over gRPC.

        Splits capacity commitment to two commitments of the same plan
        and commitment_end_time. A common use case to do that is to
        perform a downgrade e.g., in order to downgrade from 10000 slots
        to 8000, one might split 10000 capacity commitment to 2000 and
        8000, change the plan of the first one to flex and then delete
        it.

        Returns:
            Callable[[~.SplitCapacityCommitmentRequest],
                    ~.SplitCapacityCommitmentResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "split_capacity_commitment" not in self._stubs:
            self._stubs["split_capacity_commitment"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/SplitCapacityCommitment",
                request_serializer=reservation.SplitCapacityCommitmentRequest.serialize,
                response_deserializer=reservation.SplitCapacityCommitmentResponse.deserialize,
            )
        return self._stubs["split_capacity_commitment"]

    @property
    def merge_capacity_commitments(
        self
    ) -> Callable[
        [reservation.MergeCapacityCommitmentsRequest], reservation.CapacityCommitment
    ]:
        r"""Return a callable for the merge capacity commitments method over gRPC.

        Merges capacity commitments of the same plan into one. Resulting
        capacity commitment has the longer commitment_end_time out of
        the two. Attempting to merge capacity commitments of different
        plan will fail with the error code
        ``google.rpc.Code.FAILED_PRECONDITION``.

        Returns:
            Callable[[~.MergeCapacityCommitmentsRequest],
                    ~.CapacityCommitment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "merge_capacity_commitments" not in self._stubs:
            self._stubs["merge_capacity_commitments"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/MergeCapacityCommitments",
                request_serializer=reservation.MergeCapacityCommitmentsRequest.serialize,
                response_deserializer=reservation.CapacityCommitment.deserialize,
            )
        return self._stubs["merge_capacity_commitments"]

    @property
    def create_assignment(
        self
    ) -> Callable[[reservation.CreateAssignmentRequest], reservation.Assignment]:
        r"""Return a callable for the create assignment method over gRPC.

        Creates an object which allows the given project to submit jobs
        of a certain type using slots from the specified reservation.
        Currently a resource (project, folder, organization) can only
        have one assignment per {job_type, location}, and that
        reservation will be used for all jobs of the matching type.
        Within the organization, different assignments can be created on
        projects, folders or organization level. During query execution,
        the assignment is looked up at the project, folder and
        organization levels in that order. The first assignment found is
        applied to the query. When creating assignments, it does not
        matter if other assignments exist at higher levels. E.g:
        organizationA contains project1, project2. Assignments for
        organizationA, project1 and project2 could all be created,
        mapping to the same or different reservations. Returns
        ``google.rpc.Code.PERMISSION_DENIED`` if user does not have
        'bigquery.admin' permissions on the project using the
        reservation and the project that owns this reservation. Returns
        ``google.rpc.Code.INVALID_ARGUMENT`` when location of the
        assignment does not match location of the reservation.

        Returns:
            Callable[[~.CreateAssignmentRequest],
                    ~.Assignment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_assignment" not in self._stubs:
            self._stubs["create_assignment"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/CreateAssignment",
                request_serializer=reservation.CreateAssignmentRequest.serialize,
                response_deserializer=reservation.Assignment.deserialize,
            )
        return self._stubs["create_assignment"]

    @property
    def list_assignments(
        self
    ) -> Callable[
        [reservation.ListAssignmentsRequest], reservation.ListAssignmentsResponse
    ]:
        r"""Return a callable for the list assignments method over gRPC.

        Lists assignments.
        Only explicitly created assignments will be returned.
        E.g: organizationA contains project1 and project2.
        Reservation res1 exists. CreateAssignment was invoked
        previously and following assignments were created
        explicitly:
          <organizationA, res1>
          <project1, res1>
        Then this API will just return the above two assignments
        for reservation res1, and no expansion/merge will
        happen. Wildcard "-" can be used for reservations in the
        request. In that case all assignments belongs to the
        specified project and location will be listed. Note "-"
        cannot be used for projects nor locations.

        Returns:
            Callable[[~.ListAssignmentsRequest],
                    ~.ListAssignmentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_assignments" not in self._stubs:
            self._stubs["list_assignments"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/ListAssignments",
                request_serializer=reservation.ListAssignmentsRequest.serialize,
                response_deserializer=reservation.ListAssignmentsResponse.deserialize,
            )
        return self._stubs["list_assignments"]

    @property
    def delete_assignment(
        self
    ) -> Callable[[reservation.DeleteAssignmentRequest], empty.Empty]:
        r"""Return a callable for the delete assignment method over gRPC.

        Deletes a assignment. No expansion will happen.
        E.g:
        organizationA contains project1 and project2.
        Reservation res1 exists. CreateAssignment was invoked
        previously and following assignments were created
        explicitly:
          <organizationA, res1>
          <project1, res1>
        Then deletion of <organizationA, res1> won't affect
        <project1, res1>. After deletion of <organizationA,
        res1>, queries from project1 will still use res1, while
        queries from project2 will use on-demand mode.

        Returns:
            Callable[[~.DeleteAssignmentRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_assignment" not in self._stubs:
            self._stubs["delete_assignment"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/DeleteAssignment",
                request_serializer=reservation.DeleteAssignmentRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["delete_assignment"]

    @property
    def search_assignments(
        self
    ) -> Callable[
        [reservation.SearchAssignmentsRequest], reservation.SearchAssignmentsResponse
    ]:
        r"""Return a callable for the search assignments method over gRPC.

        Looks up assignments for a specified resource for a particular
        region. If the request is about a project:

        1) Assignments created on the project will be returned if they
           exist.
        2) Otherwise assignments created on the closest ancestor will be
           returned. 3) Assignments for different JobTypes will all be
           returned. Same logic applies if the request is about a
           folder. If the request is about an organization, then
           assignments created on the organization will be returned
           (organization doesn't have ancestors). Comparing to
           ListAssignments, there are some behavior differences:
        3) permission on the assignee will be verified in this API.
        4) Hierarchy lookup (project->folder->organization) happens in
           this API.
        5) Parent here is projects/\ */locations/*, instead of
           projects/*/locations/\ *reservations/*. Note "-" cannot be
           used for projects nor locations.

        Returns:
            Callable[[~.SearchAssignmentsRequest],
                    ~.SearchAssignmentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_assignments" not in self._stubs:
            self._stubs["search_assignments"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/SearchAssignments",
                request_serializer=reservation.SearchAssignmentsRequest.serialize,
                response_deserializer=reservation.SearchAssignmentsResponse.deserialize,
            )
        return self._stubs["search_assignments"]

    @property
    def move_assignment(
        self
    ) -> Callable[[reservation.MoveAssignmentRequest], reservation.Assignment]:
        r"""Return a callable for the move assignment method over gRPC.

        Moves a assignment under a new reservation. Customers
        can do this by deleting the existing assignment followed
        by creating another assignment under the new
        reservation, but this method provides a transactional
        way to do so, to make sure the assignee always has an
        associated reservation. Without the method customers
        might see some queries run on-demand which might be
        unexpected.

        Returns:
            Callable[[~.MoveAssignmentRequest],
                    ~.Assignment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "move_assignment" not in self._stubs:
            self._stubs["move_assignment"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/MoveAssignment",
                request_serializer=reservation.MoveAssignmentRequest.serialize,
                response_deserializer=reservation.Assignment.deserialize,
            )
        return self._stubs["move_assignment"]

    @property
    def get_bi_reservation(
        self
    ) -> Callable[[reservation.GetBiReservationRequest], reservation.BiReservation]:
        r"""Return a callable for the get bi reservation method over gRPC.

        Retrieves a BI reservation.

        Returns:
            Callable[[~.GetBiReservationRequest],
                    ~.BiReservation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_bi_reservation" not in self._stubs:
            self._stubs["get_bi_reservation"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/GetBiReservation",
                request_serializer=reservation.GetBiReservationRequest.serialize,
                response_deserializer=reservation.BiReservation.deserialize,
            )
        return self._stubs["get_bi_reservation"]

    @property
    def update_bi_reservation(
        self
    ) -> Callable[[reservation.UpdateBiReservationRequest], reservation.BiReservation]:
        r"""Return a callable for the update bi reservation method over gRPC.

        Updates a BI reservation. Only fields specified in the
        field_mask are updated. Singleton BI reservation always exists
        with default size 0. In order to reserve BI capacity it needs to
        be updated to an amount greater than 0. In order to release BI
        capacity reservation size must be set to 0.

        Returns:
            Callable[[~.UpdateBiReservationRequest],
                    ~.BiReservation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_bi_reservation" not in self._stubs:
            self._stubs["update_bi_reservation"] = self.grpc_channel.unary_unary(
                "/google.cloud.bigquery.reservation.v1.ReservationService/UpdateBiReservation",
                request_serializer=reservation.UpdateBiReservationRequest.serialize,
                response_deserializer=reservation.BiReservation.deserialize,
            )
        return self._stubs["update_bi_reservation"]


__all__ = ("ReservationServiceGrpcTransport",)