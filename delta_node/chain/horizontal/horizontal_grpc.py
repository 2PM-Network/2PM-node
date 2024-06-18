# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: horizontal.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

from ..transaction import transaction_pb2
from . import horizontal_pb2


class HorizontalBase(abc.ABC):

    @abc.abstractmethod
    async def CreateTask(self, stream: 'grpclib.server.Stream[horizontal_pb2.CreateTaskReq, horizontal_pb2.CreateTaskResp]') -> None:
        pass

    @abc.abstractmethod
    async def FinishTask(self, stream: 'grpclib.server.Stream[horizontal_pb2.FinishTaskReq, transaction_pb2.Transaction]') -> None:
        pass

    @abc.abstractmethod
    async def GetTask(self, stream: 'grpclib.server.Stream[horizontal_pb2.TaskReq, horizontal_pb2.TaskResp]') -> None:
        pass

    @abc.abstractmethod
    async def StartRound(self, stream: 'grpclib.server.Stream[horizontal_pb2.StartRoundReq, transaction_pb2.Transaction]') -> None:
        pass

    @abc.abstractmethod
    async def JoinRound(self, stream: 'grpclib.server.Stream[horizontal_pb2.JoinRoundReq, transaction_pb2.Transaction]') -> None:
        pass

    @abc.abstractmethod
    async def GetTaskRound(self, stream: 'grpclib.server.Stream[horizontal_pb2.TaskRoundReq, horizontal_pb2.TaskRoundResp]') -> None:
        pass

    @abc.abstractmethod
    async def SelectCandidates(self, stream: 'grpclib.server.Stream[horizontal_pb2.CandidatesReq, transaction_pb2.Transaction]') -> None:
        pass

    @abc.abstractmethod
    async def UploadSeedCommitment(self, stream: 'grpclib.server.Stream[horizontal_pb2.ShareCommitment, transaction_pb2.Transaction]') -> None:
        pass

    @abc.abstractmethod
    async def UploadSecretKeyCommitment(self, stream: 'grpclib.server.Stream[horizontal_pb2.ShareCommitment, transaction_pb2.Transaction]') -> None:
        pass

    @abc.abstractmethod
    async def GetClientPublickKeys(self, stream: 'grpclib.server.Stream[horizontal_pb2.PublicKeyReq, horizontal_pb2.PublicKeyResp]') -> None:
        pass

    @abc.abstractmethod
    async def StartCalculation(self, stream: 'grpclib.server.Stream[horizontal_pb2.CalculationReq, transaction_pb2.Transaction]') -> None:
        pass

    @abc.abstractmethod
    async def UploadResultCommitment(self, stream: 'grpclib.server.Stream[horizontal_pb2.ResultCommitment, transaction_pb2.Transaction]') -> None:
        pass

    @abc.abstractmethod
    async def GetResultCommitment(self, stream: 'grpclib.server.Stream[horizontal_pb2.ResultCommitmentReq, horizontal_pb2.ResultCommitmentResp]') -> None:
        pass

    @abc.abstractmethod
    async def StartAggregation(self, stream: 'grpclib.server.Stream[horizontal_pb2.AggregationReq, transaction_pb2.Transaction]') -> None:
        pass

    @abc.abstractmethod
    async def UploadSeed(self, stream: 'grpclib.server.Stream[horizontal_pb2.Share, transaction_pb2.Transaction]') -> None:
        pass

    @abc.abstractmethod
    async def UploadSecretKey(self, stream: 'grpclib.server.Stream[horizontal_pb2.Share, transaction_pb2.Transaction]') -> None:
        pass

    @abc.abstractmethod
    async def GetSecretShareDatas(self, stream: 'grpclib.server.Stream[horizontal_pb2.SecretShareReq, horizontal_pb2.SecretShareResp]') -> None:
        pass

    @abc.abstractmethod
    async def EndRound(self, stream: 'grpclib.server.Stream[horizontal_pb2.EndRoundReq, transaction_pb2.Transaction]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/horizontal.Horizontal/CreateTask': grpclib.const.Handler(
                self.CreateTask,
                grpclib.const.Cardinality.UNARY_UNARY,
                horizontal_pb2.CreateTaskReq,
                horizontal_pb2.CreateTaskResp,
            ),
            '/horizontal.Horizontal/FinishTask': grpclib.const.Handler(
                self.FinishTask,
                grpclib.const.Cardinality.UNARY_UNARY,
                horizontal_pb2.FinishTaskReq,
                transaction_pb2.Transaction,
            ),
            '/horizontal.Horizontal/GetTask': grpclib.const.Handler(
                self.GetTask,
                grpclib.const.Cardinality.UNARY_UNARY,
                horizontal_pb2.TaskReq,
                horizontal_pb2.TaskResp,
            ),
            '/horizontal.Horizontal/StartRound': grpclib.const.Handler(
                self.StartRound,
                grpclib.const.Cardinality.UNARY_UNARY,
                horizontal_pb2.StartRoundReq,
                transaction_pb2.Transaction,
            ),
            '/horizontal.Horizontal/JoinRound': grpclib.const.Handler(
                self.JoinRound,
                grpclib.const.Cardinality.UNARY_UNARY,
                horizontal_pb2.JoinRoundReq,
                transaction_pb2.Transaction,
            ),
            '/horizontal.Horizontal/GetTaskRound': grpclib.const.Handler(
                self.GetTaskRound,
                grpclib.const.Cardinality.UNARY_UNARY,
                horizontal_pb2.TaskRoundReq,
                horizontal_pb2.TaskRoundResp,
            ),
            '/horizontal.Horizontal/SelectCandidates': grpclib.const.Handler(
                self.SelectCandidates,
                grpclib.const.Cardinality.UNARY_UNARY,
                horizontal_pb2.CandidatesReq,
                transaction_pb2.Transaction,
            ),
            '/horizontal.Horizontal/UploadSeedCommitment': grpclib.const.Handler(
                self.UploadSeedCommitment,
                grpclib.const.Cardinality.UNARY_UNARY,
                horizontal_pb2.ShareCommitment,
                transaction_pb2.Transaction,
            ),
            '/horizontal.Horizontal/UploadSecretKeyCommitment': grpclib.const.Handler(
                self.UploadSecretKeyCommitment,
                grpclib.const.Cardinality.UNARY_UNARY,
                horizontal_pb2.ShareCommitment,
                transaction_pb2.Transaction,
            ),
            '/horizontal.Horizontal/GetClientPublickKeys': grpclib.const.Handler(
                self.GetClientPublickKeys,
                grpclib.const.Cardinality.UNARY_UNARY,
                horizontal_pb2.PublicKeyReq,
                horizontal_pb2.PublicKeyResp,
            ),
            '/horizontal.Horizontal/StartCalculation': grpclib.const.Handler(
                self.StartCalculation,
                grpclib.const.Cardinality.UNARY_UNARY,
                horizontal_pb2.CalculationReq,
                transaction_pb2.Transaction,
            ),
            '/horizontal.Horizontal/UploadResultCommitment': grpclib.const.Handler(
                self.UploadResultCommitment,
                grpclib.const.Cardinality.UNARY_UNARY,
                horizontal_pb2.ResultCommitment,
                transaction_pb2.Transaction,
            ),
            '/horizontal.Horizontal/GetResultCommitment': grpclib.const.Handler(
                self.GetResultCommitment,
                grpclib.const.Cardinality.UNARY_UNARY,
                horizontal_pb2.ResultCommitmentReq,
                horizontal_pb2.ResultCommitmentResp,
            ),
            '/horizontal.Horizontal/StartAggregation': grpclib.const.Handler(
                self.StartAggregation,
                grpclib.const.Cardinality.UNARY_UNARY,
                horizontal_pb2.AggregationReq,
                transaction_pb2.Transaction,
            ),
            '/horizontal.Horizontal/UploadSeed': grpclib.const.Handler(
                self.UploadSeed,
                grpclib.const.Cardinality.UNARY_UNARY,
                horizontal_pb2.Share,
                transaction_pb2.Transaction,
            ),
            '/horizontal.Horizontal/UploadSecretKey': grpclib.const.Handler(
                self.UploadSecretKey,
                grpclib.const.Cardinality.UNARY_UNARY,
                horizontal_pb2.Share,
                transaction_pb2.Transaction,
            ),
            '/horizontal.Horizontal/GetSecretShareDatas': grpclib.const.Handler(
                self.GetSecretShareDatas,
                grpclib.const.Cardinality.UNARY_UNARY,
                horizontal_pb2.SecretShareReq,
                horizontal_pb2.SecretShareResp,
            ),
            '/horizontal.Horizontal/EndRound': grpclib.const.Handler(
                self.EndRound,
                grpclib.const.Cardinality.UNARY_UNARY,
                horizontal_pb2.EndRoundReq,
                transaction_pb2.Transaction,
            ),
        }


class HorizontalStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateTask = grpclib.client.UnaryUnaryMethod(
            channel,
            '/horizontal.Horizontal/CreateTask',
            horizontal_pb2.CreateTaskReq,
            horizontal_pb2.CreateTaskResp,
        )
        self.FinishTask = grpclib.client.UnaryUnaryMethod(
            channel,
            '/horizontal.Horizontal/FinishTask',
            horizontal_pb2.FinishTaskReq,
            transaction_pb2.Transaction,
        )
        self.GetTask = grpclib.client.UnaryUnaryMethod(
            channel,
            '/horizontal.Horizontal/GetTask',
            horizontal_pb2.TaskReq,
            horizontal_pb2.TaskResp,
        )
        self.StartRound = grpclib.client.UnaryUnaryMethod(
            channel,
            '/horizontal.Horizontal/StartRound',
            horizontal_pb2.StartRoundReq,
            transaction_pb2.Transaction,
        )
        self.JoinRound = grpclib.client.UnaryUnaryMethod(
            channel,
            '/horizontal.Horizontal/JoinRound',
            horizontal_pb2.JoinRoundReq,
            transaction_pb2.Transaction,
        )
        self.GetTaskRound = grpclib.client.UnaryUnaryMethod(
            channel,
            '/horizontal.Horizontal/GetTaskRound',
            horizontal_pb2.TaskRoundReq,
            horizontal_pb2.TaskRoundResp,
        )
        self.SelectCandidates = grpclib.client.UnaryUnaryMethod(
            channel,
            '/horizontal.Horizontal/SelectCandidates',
            horizontal_pb2.CandidatesReq,
            transaction_pb2.Transaction,
        )
        self.UploadSeedCommitment = grpclib.client.UnaryUnaryMethod(
            channel,
            '/horizontal.Horizontal/UploadSeedCommitment',
            horizontal_pb2.ShareCommitment,
            transaction_pb2.Transaction,
        )
        self.UploadSecretKeyCommitment = grpclib.client.UnaryUnaryMethod(
            channel,
            '/horizontal.Horizontal/UploadSecretKeyCommitment',
            horizontal_pb2.ShareCommitment,
            transaction_pb2.Transaction,
        )
        self.GetClientPublickKeys = grpclib.client.UnaryUnaryMethod(
            channel,
            '/horizontal.Horizontal/GetClientPublickKeys',
            horizontal_pb2.PublicKeyReq,
            horizontal_pb2.PublicKeyResp,
        )
        self.StartCalculation = grpclib.client.UnaryUnaryMethod(
            channel,
            '/horizontal.Horizontal/StartCalculation',
            horizontal_pb2.CalculationReq,
            transaction_pb2.Transaction,
        )
        self.UploadResultCommitment = grpclib.client.UnaryUnaryMethod(
            channel,
            '/horizontal.Horizontal/UploadResultCommitment',
            horizontal_pb2.ResultCommitment,
            transaction_pb2.Transaction,
        )
        self.GetResultCommitment = grpclib.client.UnaryUnaryMethod(
            channel,
            '/horizontal.Horizontal/GetResultCommitment',
            horizontal_pb2.ResultCommitmentReq,
            horizontal_pb2.ResultCommitmentResp,
        )
        self.StartAggregation = grpclib.client.UnaryUnaryMethod(
            channel,
            '/horizontal.Horizontal/StartAggregation',
            horizontal_pb2.AggregationReq,
            transaction_pb2.Transaction,
        )
        self.UploadSeed = grpclib.client.UnaryUnaryMethod(
            channel,
            '/horizontal.Horizontal/UploadSeed',
            horizontal_pb2.Share,
            transaction_pb2.Transaction,
        )
        self.UploadSecretKey = grpclib.client.UnaryUnaryMethod(
            channel,
            '/horizontal.Horizontal/UploadSecretKey',
            horizontal_pb2.Share,
            transaction_pb2.Transaction,
        )
        self.GetSecretShareDatas = grpclib.client.UnaryUnaryMethod(
            channel,
            '/horizontal.Horizontal/GetSecretShareDatas',
            horizontal_pb2.SecretShareReq,
            horizontal_pb2.SecretShareResp,
        )
        self.EndRound = grpclib.client.UnaryUnaryMethod(
            channel,
            '/horizontal.Horizontal/EndRound',
            horizontal_pb2.EndRoundReq,
            transaction_pb2.Transaction,
        )
