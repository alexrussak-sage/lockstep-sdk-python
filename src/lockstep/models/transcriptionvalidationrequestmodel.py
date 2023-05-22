#
# Lockstep Platform SDK for Python
#
# (c) 2021-2023 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Lockstep Network <support@lockstep.io>
# @copyright  2021-2023 Lockstep, Inc.
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass

@dataclass
class TranscriptionValidationRequestModel:
    """
    Represents a transcription validation request that is used to
    validate if file is of a specific type.
    """

    transcriptionValidationRequestId: object | None = None
    groupKey: object | None = None
    statusCode: object | None = None
    created: object | None = None
    createdUserId: object | None = None
    modified: object | None = None
    modifiedUserId: object | None = None
    items: list[object] | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
