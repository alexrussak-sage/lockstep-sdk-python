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
class PayablesComingDueHeaderModel:
    """
    Contains summary information for payables that will be due soon
    """

    groupKey: str | None = None
    numberOfBillsDue: int | None = None
    numberOfVendors: int | None = None
    percentageOfTotal: float | None = None
    totalAmountDue: float | None = None
    dueDate: str | None = None

