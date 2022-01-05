#
# Lockstep Software Development Kit for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Ted Spence <tspence@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @version    2021.39
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#

from src.lockstep_api import LockstepApi
from src.models.lockstep_response import LockstepResponse
from src.models.paymentmodel import PaymentModel

class PaymentsClient:

    def __init__(self, client: LockstepApi):
        self.client = client

    """
    Retrieves the Payment specified by this unique identifier, 
    optionally including nested data sets. 

    A Payment represents money sent from one company to another. A 
    single payment may contain payments for one or more invoices; it is 
    also possible for payments to be made in advance of an invoice, for 
    example, as a deposit. The creator of the Payment is identified by 
    the `CustomerId` field, and the recipient of the Payment is 
    identified by the `CompanyId` field. Most Payments are uniquely 
    identified both by a Lockstep Platform ID number and a customer ERP 
    "key" that was generated by the system that originated the Payment. 
    Payments that have not been fully applied have a nonzero 
    `UnappliedAmount` value, which represents a deposit that has been 
    paid and not yet applied to an Invoice.

    Parameters
    ----------
    id : str
        The unique Lockstep Platform ID number of this Payment; NOT the 
        customer's ERP key
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. Available collections: Applications, 
        Notes, Attachments, CustomFields
    """
    def retrieve_payment(self, id: str, include: str) -> LockstepResponse:
        path = f"/api/v1/Payments/{id}"
        return self.client.send_request("GET", path, None, {id: str, include: str})

    """
    Updates an existing Payment with the information supplied to this 
    PATCH call. 

    The PATCH method allows you to change specific values on the object 
    while leaving other values alone. As input you should supply a list 
    of field names and new values. If you do not provide the name of a 
    field, that field will remain unchanged. This allows you to ensure 
    that you are only updating the specific fields desired. 

    A Payment represents money sent from one company to another. A 
    single payment may contain payments for one or more invoices; it is 
    also possible for payments to be made in advance of an invoice, for 
    example, as a deposit. The creator of the Payment is identified by 
    the `CustomerId` field, and the recipient of the Payment is 
    identified by the `CompanyId` field. Most Payments are uniquely 
    identified both by a Lockstep Platform ID number and a customer ERP 
    "key" that was generated by the system that originated the Payment. 
    Payments that have not been fully applied have a nonzero 
    `UnappliedAmount` value, which represents a deposit that has been 
    paid and not yet applied to an Invoice.

    Parameters
    ----------
    id : str
        The unique Lockstep Platform ID number of the Payment to update; 
        NOT the customer's ERP key
    body : object
        A list of changes to apply to this Payment
    """
    def update_payment(self, id: str, body: object) -> LockstepResponse:
        path = f"/api/v1/Payments/{id}"
        return self.client.send_request("PATCH", path, body, {id: str, body: object})

    """
    Deletes the Payment referred to by this unique identifier. 

    A Payment represents money sent from one company to another. A 
    single payment may contain payments for one or more invoices; it is 
    also possible for payments to be made in advance of an invoice, for 
    example, as a deposit. The creator of the Payment is identified by 
    the `CustomerId` field, and the recipient of the Payment is 
    identified by the `CompanyId` field. Most Payments are uniquely 
    identified both by a Lockstep Platform ID number and a customer ERP 
    "key" that was generated by the system that originated the Payment. 
    Payments that have not been fully applied have a nonzero 
    `UnappliedAmount` value, which represents a deposit that has been 
    paid and not yet applied to an Invoice.

    Parameters
    ----------
    id : str
        The unique Lockstep Platform ID number of the Payment to delete; 
        NOT the customer's ERP key
    """
    def delete_payment(self, id: str) -> LockstepResponse:
        path = f"/api/v1/Payments/{id}"
        return self.client.send_request("DELETE", path, None, {id: str})

    """
    Creates one or more Payments within this account and returns the 
    records as created. 

    A Payment represents money sent from one company to another. A 
    single payment may contain payments for one or more invoices; it is 
    also possible for payments to be made in advance of an invoice, for 
    example, as a deposit. The creator of the Payment is identified by 
    the `CustomerId` field, and the recipient of the Payment is 
    identified by the `CompanyId` field. Most Payments are uniquely 
    identified both by a Lockstep Platform ID number and a customer ERP 
    "key" that was generated by the system that originated the Payment. 
    Payments that have not been fully applied have a nonzero 
    `UnappliedAmount` value, which represents a deposit that has been 
    paid and not yet applied to an Invoice.

    Parameters
    ----------
    body : list[PaymentModel]
        The Payments to create
    """
    def create_payments(self, body: list[PaymentModel]) -> LockstepResponse:
        path = f"/api/v1/Payments"
        return self.client.send_request("POST", path, body, {body: list[PaymentModel]})

    """
    Queries Payments for this account using the specified filtering, 
    sorting, nested fetch, and pagination rules requested. 

    More information on querying can be found on the [Searchlight Query 
    Language](https://developer.lockstep.io/docs/querying-with-searchlight) 
    page on the Lockstep Developer website. 

    A Payment represents money sent from one company to another. A 
    single payment may contain payments for one or more invoices; it is 
    also possible for payments to be made in advance of an invoice, for 
    example, as a deposit. The creator of the Payment is identified by 
    the `CustomerId` field, and the recipient of the Payment is 
    identified by the `CompanyId` field. Most Payments are uniquely 
    identified both by a Lockstep Platform ID number and a customer ERP 
    "key" that was generated by the system that originated the Payment. 
    Payments that have not been fully applied have a nonzero 
    `UnappliedAmount` value, which represents a deposit that has been 
    paid and not yet applied to an Invoice.

    Parameters
    ----------
    filter : str
        The filter for this query. See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. Available collections: Applications, 
        Notes, Attachments, CustomFields
    order : str
        The sort order for this query. See See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    pageSize : int
        The page size for results (default 200). See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    pageNumber : int
        The page number for results (default 0). See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    """
    def query_payments(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse:
        path = f"/api/v1/Payments/query"
        return self.client.send_request("GET", path, None, {filter: str, include: str, order: str, pageSize: int, pageNumber: int})

    """
    Queries Payments for this account using the specified filtering, 
    sorting, nested fetch, and pagination rules requested. This query 
    endpoint provides extra data about the summary of payment 
    information. 

    More information on querying can be found on the [Searchlight Query 
    Language](https://developer.lockstep.io/docs/querying-with-searchlight) 
    page on the Lockstep Developer website. 

    A Payment represents money sent from one company to another. A 
    single payment may contain payments for one or more invoices; it is 
    also possible for payments to be made in advance of an invoice, for 
    example, as a deposit. The creator of the Payment is identified by 
    the `CustomerId` field, and the recipient of the Payment is 
    identified by the `CompanyId` field. Most Payments are uniquely 
    identified both by a Lockstep Platform ID number and a customer ERP 
    "key" that was generated by the system that originated the Payment. 
    Payments that have not been fully applied have a nonzero 
    `UnappliedAmount` value, which represents a deposit that has been 
    paid and not yet applied to an Invoice.

    Parameters
    ----------
    filter : str
        The filter for this query. See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. 

        No collections are currently available but may be offered in the 
        future
    order : str
        The sort order for this query. See See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    pageSize : int
        The page size for results (default 200). See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    pageNumber : int
        The page number for results (default 0). See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    """
    def query_payment_summary_view(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse:
        path = f"/api/v1/Payments/views/summary"
        return self.client.send_request("GET", path, None, {filter: str, include: str, order: str, pageSize: int, pageNumber: int})

    """
    Retrieves aggregated payment data from your account.

    Parameters
    ----------
    """
    def retrieve_payment_detail_header(self, ) -> LockstepResponse:
        path = f"/api/v1/Payments/views/detail-header"
        return self.client.send_request("GET", path, None, None)

    """
    Queries Payments within the Lockstep platform using the specified 
    filtering, sorting, nested fetch, and pagination rules requested. 

    More information on querying can be found on the [Searchlight Query 
    Language](https://developer.lockstep.io/docs/querying-with-searchlight) 
    page on the Lockstep Developer website. A Payment represents money 
    sent from one company to another. A single payment may contain 
    payments for one or more invoices; it is also possible for payments 
    to be made in advance of an invoice, for example, as a deposit. The 
    creator of the Payment is identified by the CustomerId field, and 
    the recipient of the Payment is identified by the CompanyId field. 
    Most Payments are uniquely identified both by a Lockstep Platform ID 
    number and a customer ERP "key" that was generated by the system 
    that originated the Payment. Payments that have not been fully 
    applied have a nonzero UnappliedAmount value, which represents a 
    deposit that has been paid and not yet applied to an Invoice.

    Parameters
    ----------
    filter : str
        The filter for this query. See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. 

        No collections are currently available but may be offered in the 
        future
    order : str
        The sort order for this query. See See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    pageSize : int
        The page size for results (default 200). See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    pageNumber : int
        The page number for results (default 0). See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    """
    def query_payment_detail_view(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse:
        path = f"/api/v1/Payments/views/detail"
        return self.client.send_request("GET", path, None, {filter: str, include: str, order: str, pageSize: int, pageNumber: int})
