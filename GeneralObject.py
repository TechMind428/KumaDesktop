# automatically generated by the FlatBuffers compiler, do not modify

# namespace: SmartCamera

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class GeneralObject(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GeneralObject()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsGeneralObject(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # GeneralObject
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # GeneralObject
    def ClassId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # GeneralObject
    def BoundingBoxType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # GeneralObject
    def BoundingBox(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

    # GeneralObject
    def Score(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def GeneralObjectStart(builder):
    builder.StartObject(4)

def Start(builder):
    GeneralObjectStart(builder)

def GeneralObjectAddClassId(builder, classId):
    builder.PrependUint32Slot(0, classId, 0)

def AddClassId(builder, classId):
    GeneralObjectAddClassId(builder, classId)

def GeneralObjectAddBoundingBoxType(builder, boundingBoxType):
    builder.PrependUint8Slot(1, boundingBoxType, 0)

def AddBoundingBoxType(builder, boundingBoxType):
    GeneralObjectAddBoundingBoxType(builder, boundingBoxType)

def GeneralObjectAddBoundingBox(builder, boundingBox):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(boundingBox), 0)

def AddBoundingBox(builder, boundingBox):
    GeneralObjectAddBoundingBox(builder, boundingBox)

def GeneralObjectAddScore(builder, score):
    builder.PrependFloat32Slot(3, score, 0.0)

def AddScore(builder, score):
    GeneralObjectAddScore(builder, score)

def GeneralObjectEnd(builder):
    return builder.EndObject()

def End(builder):
    return GeneralObjectEnd(builder)
