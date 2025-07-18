# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T02:29:44+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, List, Optional

from pydantic import BaseModel, Field, RootModel


class AdWordsLocationExtensions(BaseModel):
    adPhone: Optional[str] = Field(
        None,
        description="Required. An alternate phone number to display on AdWords location extensions instead of the location's primary phone number.",
    )


class AssociateLocationRequest(BaseModel):
    placeId: Optional[str] = Field(
        None,
        description='The association to establish. If not set, it indicates no match.',
    )


class ValueType(Enum):
    ATTRIBUTE_VALUE_TYPE_UNSPECIFIED = 'ATTRIBUTE_VALUE_TYPE_UNSPECIFIED'
    BOOL = 'BOOL'
    ENUM = 'ENUM'
    URL = 'URL'
    REPEATED_ENUM = 'REPEATED_ENUM'


class AttributeValueMetadata(BaseModel):
    displayName: Optional[str] = Field(
        None,
        description='The display name for this value, localized where available; otherwise, in English. The value display name is intended to be used in context with the attribute display name. For example, for a "WiFi" enum attribute, this could contain "Paid" to represent paid Wi-Fi.',
    )
    value: Optional[Any] = Field(None, description='The attribute value.')


class ChainName(BaseModel):
    displayName: Optional[str] = Field(
        None, description='The display name for this chain.'
    )
    languageCode: Optional[str] = Field(
        None, description='The BCP 47 code of language of the name.'
    )


class ChainUri(BaseModel):
    uri: Optional[str] = Field(None, description='The uri for this chain.')


class ClearLocationAssociationRequest(BaseModel):
    pass


class Date(BaseModel):
    day: Optional[int] = Field(
        None,
        description="Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.",
    )
    month: Optional[int] = Field(
        None,
        description='Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.',
    )
    year: Optional[int] = Field(
        None,
        description='Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.',
    )


class Empty(BaseModel):
    pass


class Label(BaseModel):
    description: Optional[str] = Field(
        None, description='Optional. Description of the price list, section, or item.'
    )
    displayName: Optional[str] = Field(
        None, description='Required. Display name for the price list, section, or item.'
    )
    languageCode: Optional[str] = Field(
        None,
        description='Optional. The BCP-47 language code that these strings apply for. Only one set of labels may be set per language.',
    )


class LatLng(BaseModel):
    latitude: Optional[float] = Field(
        None,
        description='The latitude in degrees. It must be in the range [-90.0, +90.0].',
    )
    longitude: Optional[float] = Field(
        None,
        description='The longitude in degrees. It must be in the range [-180.0, +180.0].',
    )


class Metadata(BaseModel):
    canDelete: Optional[bool] = Field(
        None,
        description='Output only. Indicates whether the location can be deleted using the API.',
    )
    canHaveBusinessCalls: Optional[bool] = Field(
        None,
        description='Output only. Indicates if the listing is eligible for business calls.',
    )
    canHaveFoodMenus: Optional[bool] = Field(
        None,
        description='Output only. Indicates if the listing is eligible for food menu.',
    )
    canModifyServiceList: Optional[bool] = Field(
        None,
        description='Output only. Indicates if the listing can modify the service list.',
    )
    canOperateHealthData: Optional[bool] = Field(
        None,
        description='Output only. Indicates whether the location can operate on Health data.',
    )
    canOperateLocalPost: Optional[bool] = Field(
        None,
        description='Output only. Indicates if the listing can manage local posts.',
    )
    canOperateLodgingData: Optional[bool] = Field(
        None,
        description='Output only. Indicates whether the location can operate on Lodging data.',
    )
    duplicateLocation: Optional[str] = Field(
        None,
        description='Output only. The location resource that this location duplicates.',
    )
    hasGoogleUpdated: Optional[bool] = Field(
        None,
        description="Output only. Indicates whether the place ID associated with this location has updates that need to be updated or rejected by the client. If this boolean is set, you should call the `getGoogleUpdated` method to lookup information that's needs to be verified.",
    )
    hasPendingEdits: Optional[bool] = Field(
        None,
        description="Output only. Indicates whether any of this Location's properties are in the edit pending state.",
    )
    hasVoiceOfMerchant: Optional[bool] = Field(
        None,
        description='Output only. Indicates if the listing has Voice of Merchant. If this boolean is false, you should call the locations.getVoiceOfMerchantState API to get details as to why they do not have Voice of Merchant.',
    )
    mapsUri: Optional[str] = Field(
        None, description='Output only. A link to the location on Maps.'
    )
    newReviewUri: Optional[str] = Field(
        None,
        description='Output only. A link to the page on Google Search where a customer can leave a review for the location.',
    )
    placeId: Optional[str] = Field(
        None,
        description='Output only. If this locationappears on Google Maps, this field is populated with the place ID for the location. This ID can be used in various Places APIs. This field can be set during Create calls, but not for Update.',
    )


class Money(BaseModel):
    currencyCode: Optional[str] = Field(
        None, description='The three-letter currency code defined in ISO 4217.'
    )
    nanos: Optional[int] = Field(
        None,
        description='Number of nano (10^-9) units of the amount. The value must be between -999,999,999 and +999,999,999 inclusive. If `units` is positive, `nanos` must be positive or zero. If `units` is zero, `nanos` can be positive, zero, or negative. If `units` is negative, `nanos` must be negative or zero. For example $-1.75 is represented as `units`=-1 and `nanos`=-750,000,000.',
    )
    units: Optional[str] = Field(
        None,
        description='The whole units of the amount. For example if `currencyCode` is `"USD"`, then 1 unit is one US dollar.',
    )


class MoreHoursType(BaseModel):
    displayName: Optional[str] = Field(
        None,
        description='Output only. The human-readable English display name for the hours type.',
    )
    hoursTypeId: Optional[str] = Field(
        None,
        description='Output only. A stable ID provided by Google for this hours type.',
    )
    localizedDisplayName: Optional[str] = Field(
        None,
        description='Output only. The human-readable localized display name for the hours type.',
    )


class Status(Enum):
    OPEN_FOR_BUSINESS_UNSPECIFIED = 'OPEN_FOR_BUSINESS_UNSPECIFIED'
    OPEN = 'OPEN'
    CLOSED_PERMANENTLY = 'CLOSED_PERMANENTLY'
    CLOSED_TEMPORARILY = 'CLOSED_TEMPORARILY'


class OpenInfo(BaseModel):
    canReopen: Optional[bool] = Field(
        None,
        description='Output only. Indicates whether this business is eligible for re-open.',
    )
    openingDate: Optional[Date] = Field(
        None,
        description='Optional. The date on which the location first opened. If the exact day is not known, month and year only can be provided. The date must be in the past or be no more than one year in the future.',
    )
    status: Optional[Status] = Field(
        None,
        description='Required. Indicates whether or not the Location is currently open for business. All locations are open by default, unless updated to be closed.',
    )


class PhoneNumbers(BaseModel):
    additionalPhones: Optional[List[str]] = Field(
        None,
        description='Optional. Up to two phone numbers (mobile or landline, no fax) at which your business can be called, in addition to your primary phone number.',
    )
    primaryPhone: Optional[str] = Field(
        None,
        description='Required. A phone number that connects to your individual business location as directly as possible. Use a local phone number instead of a central, call center helpline number whenever possible.',
    )


class PlaceInfo(BaseModel):
    placeId: Optional[str] = Field(
        None,
        description='Required. The ID of the place. Must correspond to a region. (https://developers.google.com/places/web-service/supported_types#table3)',
    )
    placeName: Optional[str] = Field(
        None,
        description='Required. The localized name of the place. For example, `Scottsdale, AZ`.',
    )


class Places(BaseModel):
    placeInfos: Optional[List[PlaceInfo]] = Field(
        None,
        description='The areas represented by place IDs. Limited to a maximum of 20 places.',
    )


class PostalAddress(BaseModel):
    addressLines: Optional[List[str]] = Field(
        None,
        description='Unstructured address lines describing the lower levels of an address. Because values in address_lines do not have type information and may sometimes contain multiple values in a single field (e.g. "Austin, TX"), it is important that the line order is clear. The order of address lines should be "envelope order" for the country/region of the address. In places where this can vary (e.g. Japan), address_language is used to make it explicit (e.g. "ja" for large-to-small ordering and "ja-Latn" or "en" for small-to-large). This way, the most specific line of an address can be selected based on the language. The minimum permitted structural representation of an address consists of a region_code with all remaining information placed in the address_lines. It would be possible to format such an address very approximately without geocoding, but no semantic reasoning could be made about any of the address components until it was at least partially resolved. Creating an address only containing a region_code and address_lines, and then geocoding is the recommended way to handle completely unstructured addresses (as opposed to guessing which parts of the address should be localities or administrative areas).',
    )
    administrativeArea: Optional[str] = Field(
        None,
        description='Optional. Highest administrative subdivision which is used for postal addresses of a country or region. For example, this can be a state, a province, an oblast, or a prefecture. Specifically, for Spain this is the province and not the autonomous community (e.g. "Barcelona" and not "Catalonia"). Many countries don\'t use an administrative area in postal addresses. E.g. in Switzerland this should be left unpopulated.',
    )
    languageCode: Optional[str] = Field(
        None,
        description='Optional. BCP-47 language code of the contents of this address (if known). This is often the UI language of the input form or is expected to match one of the languages used in the address\' country/region, or their transliterated equivalents. This can affect formatting in certain countries, but is not critical to the correctness of the data and will never affect any validation or other non-formatting related operations. If this value is not known, it should be omitted (rather than specifying a possibly incorrect default). Examples: "zh-Hant", "ja", "ja-Latn", "en".',
    )
    locality: Optional[str] = Field(
        None,
        description='Optional. Generally refers to the city/town portion of the address. Examples: US city, IT comune, UK post town. In regions of the world where localities are not well defined or do not fit into this structure well, leave locality empty and use address_lines.',
    )
    organization: Optional[str] = Field(
        None, description='Optional. The name of the organization at the address.'
    )
    postalCode: Optional[str] = Field(
        None,
        description='Optional. Postal code of the address. Not all countries use or require postal codes to be present, but where they are used, they may trigger additional validation with other parts of the address (e.g. state/zip validation in the U.S.A.).',
    )
    recipients: Optional[List[str]] = Field(
        None,
        description='Optional. The recipient at the address. This field may, under certain circumstances, contain multiline information. For example, it might contain "care of" information.',
    )
    regionCode: Optional[str] = Field(
        None,
        description='Required. CLDR region code of the country/region of the address. This is never inferred and it is up to the user to ensure the value is correct. See https://cldr.unicode.org/ and https://www.unicode.org/cldr/charts/30/supplemental/territory_information.html for details. Example: "CH" for Switzerland.',
    )
    revision: Optional[int] = Field(
        None,
        description='The schema revision of the `PostalAddress`. This must be set to 0, which is the latest revision. All new revisions **must** be backward compatible with old revisions.',
    )
    sortingCode: Optional[str] = Field(
        None,
        description='Optional. Additional, country-specific, sorting code. This is not used in most regions. Where it is used, the value is either a string like "CEDEX", optionally followed by a number (e.g. "CEDEX 7"), or just a number alone, representing the "sector code" (Jamaica), "delivery area indicator" (Malawi) or "post office indicator" (e.g. Côte d\'Ivoire).',
    )
    sublocality: Optional[str] = Field(
        None,
        description='Optional. Sublocality of the address. For example, this can be neighborhoods, boroughs, districts.',
    )


class Profile(BaseModel):
    description: Optional[str] = Field(
        None,
        description='Required. Description of the location in your own voice, not editable by anyone else.',
    )


class RelationType(Enum):
    RELATION_TYPE_UNSPECIFIED = 'RELATION_TYPE_UNSPECIFIED'
    DEPARTMENT_OF = 'DEPARTMENT_OF'
    INDEPENDENT_ESTABLISHMENT_IN = 'INDEPENDENT_ESTABLISHMENT_IN'


class RelevantLocation(BaseModel):
    placeId: Optional[str] = Field(
        None,
        description='Required. Specify the location that is on the other side of the relation by its placeID.',
    )
    relationType: Optional[RelationType] = Field(
        None, description='Required. The type of the relationship.'
    )


class RepeatedEnumAttributeValue(BaseModel):
    setValues: Optional[List[str]] = Field(
        None, description='Enum values that are set.'
    )
    unsetValues: Optional[List[str]] = Field(
        None, description='Enum values that are unset.'
    )


class BusinessType(Enum):
    BUSINESS_TYPE_UNSPECIFIED = 'BUSINESS_TYPE_UNSPECIFIED'
    CUSTOMER_LOCATION_ONLY = 'CUSTOMER_LOCATION_ONLY'
    CUSTOMER_AND_BUSINESS_LOCATION = 'CUSTOMER_AND_BUSINESS_LOCATION'


class ServiceAreaBusiness(BaseModel):
    businessType: Optional[BusinessType] = Field(
        None, description='Required. Indicates the type of the service area business.'
    )
    places: Optional[Places] = Field(
        None,
        description='The area that this business serves defined through a set of places.',
    )
    regionCode: Optional[str] = Field(
        None,
        description='Immutable. CLDR region code of the country/region that this service area business is based in. See http://cldr.unicode.org/ and http://www.unicode.org/cldr/charts/30/supplemental/territory_information.html for details. Example: "CH" for Switzerland. This field is required for CUSTOMER_LOCATION_ONLY businesses, and is ignored otherwise. The region specified here can be different from regions for the areas that this business serves (e.g. service area businesses that provide services in regions other than the one that they are based in). If this location requires verification after creation, the address provided for verification purposes *must* be located within this region, and the business owner or their authorized representative *must* be able to receive postal mail at the provided verification address.',
    )


class ServiceType(BaseModel):
    displayName: Optional[str] = Field(
        None,
        description='Output only. The human-readable display name for the service type.',
    )
    serviceTypeId: Optional[str] = Field(
        None,
        description='Output only. A stable ID (provided by Google) for this service type.',
    )


class StructuredServiceItem(BaseModel):
    description: Optional[str] = Field(
        None,
        description='Optional. Description of structured service item. The character limit is 300.',
    )
    serviceTypeId: Optional[str] = Field(
        None,
        description='Required. The `service_type_id` field is a Google provided unique ID that can be found in `ServiceType`. This information is provided by `BatchGetCategories` rpc service.',
    )


class TimeOfDay(BaseModel):
    hours: Optional[int] = Field(
        None,
        description='Hours of day in 24 hour format. Should be from 0 to 23. An API may choose to allow the value "24:00:00" for scenarios like business closing time.',
    )
    minutes: Optional[int] = Field(
        None, description='Minutes of hour of day. Must be from 0 to 59.'
    )
    nanos: Optional[int] = Field(
        None,
        description='Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999.',
    )
    seconds: Optional[int] = Field(
        None,
        description='Seconds of minutes of the time. Must normally be from 0 to 59. An API may allow the value 60 if it allows leap-seconds.',
    )


class CloseDay(Enum):
    DAY_OF_WEEK_UNSPECIFIED = 'DAY_OF_WEEK_UNSPECIFIED'
    MONDAY = 'MONDAY'
    TUESDAY = 'TUESDAY'
    WEDNESDAY = 'WEDNESDAY'
    THURSDAY = 'THURSDAY'
    FRIDAY = 'FRIDAY'
    SATURDAY = 'SATURDAY'
    SUNDAY = 'SUNDAY'


class OpenDay(Enum):
    DAY_OF_WEEK_UNSPECIFIED = 'DAY_OF_WEEK_UNSPECIFIED'
    MONDAY = 'MONDAY'
    TUESDAY = 'TUESDAY'
    WEDNESDAY = 'WEDNESDAY'
    THURSDAY = 'THURSDAY'
    FRIDAY = 'FRIDAY'
    SATURDAY = 'SATURDAY'
    SUNDAY = 'SUNDAY'


class TimePeriod(BaseModel):
    closeDay: Optional[CloseDay] = Field(
        None, description='Required. Indicates the day of the week this period ends on.'
    )
    closeTime: Optional[TimeOfDay] = Field(
        None,
        description='Required. Valid values are 00:00-24:00, where 24:00 represents midnight at the end of the specified day field.',
    )
    openDay: Optional[OpenDay] = Field(
        None,
        description='Required. Indicates the day of the week this period starts on.',
    )
    openTime: Optional[TimeOfDay] = Field(
        None,
        description='Required. Valid values are 00:00-24:00, where 24:00 represents midnight at the end of the specified day field.',
    )


class UriAttributeValue(BaseModel):
    uri: Optional[str] = Field(
        None, description='Required. The proposed URI value for this attribute.'
    )


class FieldXgafv(Enum):
    field_1 = '1'
    field_2 = '2'


class Alt(Enum):
    json = 'json'
    media = 'media'
    proto = 'proto'


class View(Enum):
    CATEGORY_VIEW_UNSPECIFIED = 'CATEGORY_VIEW_UNSPECIFIED'
    BASIC = 'BASIC'
    FULL = 'FULL'


class Names(RootModel[List[str]]):
    root: List[str]


class Attribute(BaseModel):
    name: Optional[str] = Field(
        None, description='Required. The resource name for this attribute.'
    )
    repeatedEnumValue: Optional[RepeatedEnumAttributeValue] = Field(
        None,
        description='When the attribute value type is REPEATED_ENUM, this contains the attribute value, and the other values fields must be empty.',
    )
    uriValues: Optional[List[UriAttributeValue]] = Field(
        None,
        description='When the attribute value type is URL, this field contains the value(s) for this attribute, and the other values fields must be empty.',
    )
    valueType: Optional[ValueType] = Field(
        None,
        description='Output only. The type of value that this attribute contains. This should be used to determine how to interpret the value.',
    )
    values: Optional[List] = Field(
        None,
        description='The values for this attribute. The type of the values supplied must match that expected for that attribute. This is a repeated field where multiple attribute values may be provided. Attribute types only support one value.',
    )


class AttributeMetadata(BaseModel):
    deprecated: Optional[bool] = Field(
        None,
        description='If true, the attribute is deprecated and should no longer be used. If deprecated, updating this attribute will not result in an error, but updates will not be saved. At some point after being deprecated, the attribute will be removed entirely and it will become an error.',
    )
    displayName: Optional[str] = Field(
        None,
        description='The localized display name for the attribute, if available; otherwise, the English display name.',
    )
    groupDisplayName: Optional[str] = Field(
        None,
        description='The localized display name of the group that contains this attribute, if available; otherwise, the English group name. Related attributes are collected into a group and should be displayed together under the heading given here.',
    )
    parent: Optional[str] = Field(
        None, description='The unique identifier for the attribute.'
    )
    repeatable: Optional[bool] = Field(
        None,
        description='If true, the attribute supports multiple values. If false, only a single value should be provided.',
    )
    valueMetadata: Optional[List[AttributeValueMetadata]] = Field(
        None,
        description='For some types of attributes (for example, enums), a list of supported values and corresponding display names for those values is provided.',
    )
    valueType: Optional[ValueType] = Field(
        None,
        description='The value type for the attribute. Values set and retrieved should be expected to be of this type.',
    )


class Attributes(BaseModel):
    attributes: Optional[List[Attribute]] = Field(
        None, description='A collection of attributes that need to be updated.'
    )
    name: Optional[str] = Field(
        None,
        description='Required. Google identifier for this location in the form of `locations/{location_id}/attributes`.',
    )


class BusinessHours(BaseModel):
    periods: Optional[List[TimePeriod]] = Field(
        None,
        description='Required. A collection of times that this location is open for business. Each period represents a range of hours when the location is open during the week.',
    )


class Category(BaseModel):
    displayName: Optional[str] = Field(
        None,
        description='Output only. The human-readable name of the category. This is set when reading the location. When modifying the location, `category_id` must be set.',
    )
    moreHoursTypes: Optional[List[MoreHoursType]] = Field(
        None,
        description='Output only. More hours types that are available for this business category.',
    )
    name: Optional[str] = Field(
        None,
        description='Required. A stable ID (provided by Google) for this category. The value must be specified when modifying the category (when creating or updating a location).',
    )
    serviceTypes: Optional[List[ServiceType]] = Field(
        None,
        description='Output only. A list of all the service types that are available for this business category.',
    )


class Chain(BaseModel):
    chainNames: Optional[List[ChainName]] = Field(
        None, description='Names of the chain.'
    )
    locationCount: Optional[int] = Field(
        None, description='Number of locations that are part of this chain.'
    )
    name: Optional[str] = Field(
        None,
        description="Required. The chain's resource name, in the format `chains/{chain_id}`.",
    )
    websites: Optional[List[ChainUri]] = Field(
        None, description='Websites of the chain.'
    )


class FreeFormServiceItem(BaseModel):
    category: Optional[str] = Field(
        None,
        description="Required. This field represents the category name (i.e. the category's stable ID). The `category` and `service_type_id` should match the possible combinations provided in the `Category` message.",
    )
    label: Optional[Label] = Field(
        None,
        description='Required. Language-tagged labels for the item. We recommend that item names be 140 characters or less, and descriptions 250 characters or less. This field should only be set if the input is a custom service item. Standardized service types should be updated via service_type_id.',
    )


class ListAttributeMetadataResponse(BaseModel):
    attributeMetadata: Optional[List[AttributeMetadata]] = Field(
        None,
        description='A collection of attribute metadata for the available attributes.',
    )
    nextPageToken: Optional[str] = Field(
        None,
        description='If the number of attributes exceeded the requested page size, this field will be populated with a token to fetch the next page of attributes on a subsequent call to `attributes.list`. If there are no more attributes, this field will not be present in the response.',
    )


class ListCategoriesResponse(BaseModel):
    categories: Optional[List[Category]] = Field(
        None, description='The matching categories based on the requested parameters.'
    )
    nextPageToken: Optional[str] = Field(
        None,
        description='If the number of categories exceeded the requested page size, this field will be populated with a token to fetch the next page of categories on a subsequent call to `ListCategories`.',
    )


class MoreHours(BaseModel):
    hoursTypeId: Optional[str] = Field(
        None,
        description='Required. Type of hours. Clients should call {#link businessCategories:BatchGet} to get supported hours types for categories of their locations.',
    )
    periods: Optional[List[TimePeriod]] = Field(
        None,
        description='Required. A collection of times that this location is open. Each period represents a range of hours when the location is open during the week.',
    )


class RelationshipData(BaseModel):
    childrenLocations: Optional[List[RelevantLocation]] = Field(
        None,
        description='The list of children locations that this location has relations with.',
    )
    parentChain: Optional[str] = Field(
        None,
        description='The resource name of the Chain that this location is member of. How to find Chain ID',
    )
    parentLocation: Optional[RelevantLocation] = Field(
        None, description='The parent location that this location has relations with.'
    )


class SearchChainsResponse(BaseModel):
    chains: Optional[List[Chain]] = Field(
        None,
        description='Chains that match the queried chain_display_name in SearchChainsRequest. If there are no matches, this field will be empty. Results are listed in order of relevance.',
    )


class ServiceItem(BaseModel):
    freeFormServiceItem: Optional[FreeFormServiceItem] = Field(
        None,
        description='Optional. This field will be set case of free-form services data.',
    )
    price: Optional[Money] = Field(
        None,
        description='Optional. Represents the monetary price of the service item. We recommend that currency_code and units should be set when including a price. This will be treated as a fixed price for the service item.',
    )
    structuredServiceItem: Optional[StructuredServiceItem] = Field(
        None,
        description='Optional. This field will be set case of structured services data.',
    )


class SpecialHourPeriod(BaseModel):
    closeTime: Optional[TimeOfDay] = Field(
        None,
        description='Optional. Valid values are 00:00-24:00, where 24:00 represents midnight at the end of the specified day field. Must be specified if `closed` is false.',
    )
    closed: Optional[bool] = Field(
        None,
        description='Optional. If true, `end_date`, `open_time`, and `close_time` are ignored, and the date specified in `start_date` is treated as the location being closed for the entire day.',
    )
    endDate: Optional[Date] = Field(
        None,
        description='Optional. The calendar date this special hour period ends on. If `end_date` field is not set, default to the date specified in `start_date`. If set, this field must be equal to or at most 1 day after `start_date`.',
    )
    openTime: Optional[TimeOfDay] = Field(
        None,
        description='Optional. Valid values are 00:00-24:00 where 24:00 represents midnight at the end of the specified day field. Must be specified if `closed` is false.',
    )
    startDate: Optional[Date] = Field(
        None,
        description='Required. The calendar date this special hour period starts on.',
    )


class SpecialHours(BaseModel):
    specialHourPeriods: Optional[List[SpecialHourPeriod]] = Field(
        None,
        description="Required. A list of exceptions to the business's regular hours.",
    )


class BatchGetCategoriesResponse(BaseModel):
    categories: Optional[List[Category]] = Field(
        None,
        description='Categories that match the GConcept ids provided in the request. They will not come in the same order as category ids in the request.',
    )


class Categories(BaseModel):
    additionalCategories: Optional[List[Category]] = Field(
        None,
        description="Optional. Additional categories to describe your business. Categories help your customers find accurate, specific results for services they're interested in. To keep your business information accurate and live, make sure that you use as few categories as possible to describe your overall core business. Choose categories that are as specific as possible, but representative of your main business.",
    )
    primaryCategory: Optional[Category] = Field(
        None,
        description='Required. Category that best describes the core business this location engages in.',
    )


class Location(BaseModel):
    adWordsLocationExtensions: Optional[AdWordsLocationExtensions] = Field(
        None,
        description='Optional. Additional information that is surfaced in AdWords.',
    )
    categories: Optional[Categories] = Field(
        None,
        description='Optional. The different categories that describe the business.',
    )
    labels: Optional[List[str]] = Field(
        None,
        description='Optional. A collection of free-form strings to allow you to tag your business. These labels are NOT user facing; only you can see them. Must be between 1-255 characters per label.',
    )
    languageCode: Optional[str] = Field(
        None,
        description='Immutable. The language of the location. Set during creation and not updateable.',
    )
    latlng: Optional[LatLng] = Field(
        None,
        description='Optional. User-provided latitude and longitude. When creating a location, this field is ignored if the provided address geocodes successfully. This field is only returned on get requests if the user-provided `latlng` value was accepted during create, or the `latlng` value was updated through the Google Business Profile website. This field can only be updated by approved clients.',
    )
    metadata: Optional[Metadata] = Field(
        None, description='Output only. Additional non-user-editable information.'
    )
    moreHours: Optional[List[MoreHours]] = Field(
        None,
        description="Optional. More hours for a business's different departments or specific customers.",
    )
    name: Optional[str] = Field(
        None,
        description='Google identifier for this location in the form: `locations/{location_id}`.',
    )
    openInfo: Optional[OpenInfo] = Field(
        None,
        description='Optional. A flag that indicates whether the location is currently open for business.',
    )
    phoneNumbers: Optional[PhoneNumbers] = Field(
        None,
        description='Optional. The different phone numbers that customers can use to get in touch with the business.',
    )
    profile: Optional[Profile] = Field(
        None,
        description='Optional. Describes your business in your own voice and shares with users the unique story of your business and offerings. This field is required for all categories except lodging categories (e.g. hotels, motels, inns).',
    )
    regularHours: Optional[BusinessHours] = Field(
        None, description='Optional. Operating hours for the business.'
    )
    relationshipData: Optional[RelationshipData] = Field(
        None, description='Optional. All locations and chain related to this one.'
    )
    serviceArea: Optional[ServiceAreaBusiness] = Field(
        None,
        description="Optional. Service area businesses provide their service at the customer's location. If this business is a service area business, this field describes the area(s) serviced by the business.",
    )
    serviceItems: Optional[List[ServiceItem]] = Field(
        None,
        description='Optional. List of services supported by merchants. A service can be haircut, install water heater, etc. Duplicated service items will be removed automatically.',
    )
    specialHours: Optional[SpecialHours] = Field(
        None,
        description='Optional. Special hours for the business. This typically includes holiday hours, and other times outside of regular operating hours. These override regular business hours. This field cannot be set without regular hours.',
    )
    storeCode: Optional[str] = Field(
        None,
        description='Optional. External identifier for this location, which must be unique within a given account. This is a means of associating the location with your own records.',
    )
    storefrontAddress: Optional[PostalAddress] = Field(
        None,
        description='Optional. A precise, accurate address to describe your business location. PO boxes or mailboxes located at remote locations are not acceptable. At this time, you can specify a maximum of five `address_lines` values in the address. This field should only be set for businesses that have a storefront. This field should not be set for locations of type `CUSTOMER_LOCATION_ONLY`.',
    )
    title: Optional[str] = Field(
        None,
        description='Required. Location name should reflect your business\'s real-world name, as used consistently on your storefront, website, and stationery, and as known to customers. Any additional information, when relevant, can be included in other fields of the resource (for example, `Address`, `Categories`). Don\'t add unnecessary information to your name (for example, prefer "Google" over "Google Inc. - Mountain View Corporate Headquarters"). Don\'t include marketing taglines, store codes, special characters, hours or closed/open status, phone numbers, website URLs, service/product information, location/address or directions, or containment information (for example, "Chase ATM in Duane Reade").',
    )
    websiteUri: Optional[str] = Field(
        None,
        description='Optional. A URL for this business. If possible, use a URL that represents this individual business location instead of a generic website/URL that represents all locations, or the brand.',
    )


class SearchGoogleLocationsRequest(BaseModel):
    location: Optional[Location] = Field(
        None,
        description='Location to search for. If provided, will find locations which match the provided location details.',
    )
    pageSize: Optional[int] = Field(
        None,
        description='The number of matches to return. The default value is 3, with a maximum of 10. Note that latency may increase if more are requested. There is no pagination.',
    )
    query: Optional[str] = Field(
        None,
        description='Text query to search for. The search results from a query string will be less accurate than if providing an exact location, but can provide more inexact matches.',
    )


class GoogleLocation(BaseModel):
    location: Optional[Location] = Field(
        None,
        description='The sparsely populated Location information. This field can be re-used in CreateLocation if it is not currently claimed by a user.',
    )
    name: Optional[str] = Field(
        None,
        description='Resource name of this GoogleLocation, in the format `googleLocations/{googleLocationId}`.',
    )
    requestAdminRightsUri: Optional[str] = Field(
        None,
        description='A URL that will redirect the user to the request admin rights UI. This field is only present if the location has already been claimed by any user, including the current user.',
    )


class GoogleUpdatedLocation(BaseModel):
    diffMask: Optional[str] = Field(None, description='The fields that Google updated.')
    location: Optional[Location] = Field(
        None, description='The Google-updated version of this location.'
    )
    pendingMask: Optional[str] = Field(
        None,
        description="The fields that have pending edits that haven't yet been pushed to Maps and Search.",
    )


class ListLocationsResponse(BaseModel):
    locations: Optional[List[Location]] = Field(None, description='The locations.')
    nextPageToken: Optional[str] = Field(
        None,
        description='If the number of locations exceeded the requested page size, this field is populated with a token to fetch the next page of locations on a subsequent call to `ListLocations`. If there are no more locations, this field is not present in the response.',
    )
    totalSize: Optional[int] = Field(
        None,
        description='The approximate number of Locations in the list irrespective of pagination.',
    )


class SearchGoogleLocationsResponse(BaseModel):
    googleLocations: Optional[List[GoogleLocation]] = Field(
        None,
        description='A collection of GoogleLocations that are potential matches to the specified request, listed in order from most to least accuracy.',
    )
