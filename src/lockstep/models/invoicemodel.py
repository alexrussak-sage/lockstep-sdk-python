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
class InvoiceModel:
    """
    An Invoice represents a bill sent from one company to another. The
    creator of the invoice is identified by the `CompanyId` field, and
    the recipient of the invoice is identified by the `CustomerId`
    field. Most invoices are uniquely identified both by a Lockstep
    Platform ID number and a customer ERP "key" that was generated by
    the system that originated the invoice. Invoices have a total amount
    and a due date, and when some payments have been made on the Invoice
    the `TotalAmount` and the `OutstandingBalanceAmount` may be
    different.
    """

    groupKey: object | None = None
    invoiceId: object | None = None
    companyId: object | None = None
    customerId: object | None = None
    erpKey: object | None = None
    purchaseOrderCode: object | None = None
    referenceCode: object | None = None
    salespersonCode: object | None = None
    salespersonName: object | None = None
    invoiceTypeCode: object | None = None
    invoiceStatusCode: object | None = None
    termsCode: object | None = None
    specialTerms: object | None = None
    currencyCode: object | None = None
    totalAmount: object | None = None
    salesTaxAmount: object | None = None
    discountAmount: object | None = None
    outstandingBalanceAmount: object | None = None
    invoiceDate: object | None = None
    discountDate: object | None = None
    postedDate: object | None = None
    invoiceClosedDate: object | None = None
    paymentDueDate: object | None = None
    importedDate: object | None = None
    primaryOriginAddressId: object | None = None
    primaryBillToAddressId: object | None = None
    primaryShipToAddressId: object | None = None
    created: object | None = None
    createdUserId: object | None = None
    modified: object | None = None
    modifiedUserId: object | None = None
    appEnrollmentId: object | None = None
    isVoided: object | None = None
    inDispute: object | None = None
    excludeFromAging: object | None = None
    preferredDeliveryMethod: object | None = None
    currencyRate: object | None = None
    baseCurrencyTotalAmount: object | None = None
    baseCurrencySalesTaxAmount: object | None = None
    baseCurrencyDiscountAmount: object | None = None
    baseCurrencyOutstandingBalanceAmount: object | None = None
    erpWriteStatus: object | None = None
    erpWriteStatusName: object | None = None
    sourceModifiedDate: object | None = None
    addresses: list[object] | None = None
    lines: list[object] | None = None
    payments: list[object] | None = None
    notes: list[object] | None = None
    attachments: list[object] | None = None
    company: object | None = None
    customer: object | None = None
    customerPrimaryContact: object | None = None
    creditMemos: list[object] | None = None
    customFieldValues: list[object] | None = None
    customFieldDefinitions: list[object] | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
