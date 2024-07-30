class RankInfo(BaseModel):
    rank: Optional[str] = Field(None, alias="rank")
    rankValue: Optional[str] = Field(None, alias="rankValue")
    dateUpdated: Optional[int] = Field(None, alias="dateUpdated")


class Status(BaseModel):
    id: Optional[int] = Field(None, alias="id")
    title: Optional[str] = Field(None, alias="title")
    value: Optional[str] = Field(None, alias="value")
    description: Optional[str] = Field(None, alias="description")
    color: Optional[str] = Field(None, alias="color")
    additional: Optional[List] = Field(None, alias="additional")


class ModerationStatus(BaseModel):
    title: Optional[str] = Field(None, alias="title")
    color: Optional[str] = Field(None, alias="color")
    value: Optional[str] = Field(None, alias="value")


class CommissionDto(BaseModel):
    minCommission: Optional[float] = Field(None, alias="minCommission")
    maxCommission: Optional[float] = Field(None, alias="maxCommission")


class Sku(BaseModel):
    skuTitle: Optional[str] = Field(None, alias="skuTitle")
    skuFullTitle: Optional[str] = Field(None, alias="skuFullTitle")
    productTitle: Optional[str] = Field(None, alias="productTitle")
    skuId: Optional[int] = Field(None, alias="skuId")
    quantityCreated: Optional[int] = Field(None, alias="quantityCreated")
    quantityActive: Optional[int] = Field(None, alias="quantityActive")
    quantityFbs: Optional[int] = Field(None, alias="quantityFbs")
    quantityAdditional: Optional[int] = Field(None, alias="quantityAdditional")
    quantityOnPhotoStudio: Optional[int] = Field(
        None, alias="quantityOnPhotoStudio"
    )
    quantityArchived: Optional[int] = Field(None, alias="quantityArchived")
    quantitySold: Optional[int] = Field(None, alias="quantitySold")
    quantityReturned: Optional[int] = Field(None, alias="quantityReturned")
    quantityDefected: Optional[int] = Field(None, alias="quantityDefected")
    quantityPending: Optional[int] = Field(None, alias="quantityPending")
    returnedPercentage: Optional[float] = Field(None, alias="returnedPercentage")
    barcode: Optional[int] = Field(None, alias="barcode")
    archived: Optional[bool] = Field(None, alias="archived")
    commission: Optional[float] = Field(None, alias="commission")
    characteristics: Optional[str] = Field(None, alias="characteristics")
    purchasePrice: Optional[None] = Field(None, alias="purchasePrice")
    price: Optional[float] = Field(None, alias="price")
    rankInfo: Optional[RankInfo] = Field(None, alias="rankInfo")
    discountPrice: Optional[float] = Field(None, alias="discountPrice")
    article: Optional[None] = Field(None, alias="article")
    turnover: Optional[float] = Field(None, alias="turnover")
    paidStorageCost: Optional[float] = Field(None, alias="paidStorageCost")
    length: Optional[int] = Field(None, alias="length")
    width: Optional[int] = Field(None, alias="width")
    height: Optional[int] = Field(None, alias="height")
    paidStorageVolume: Optional[float] = Field(None, alias="paidStorageVolume")
    paidStorageQuantity: Optional[int] = Field(None, alias="paidStorageQuantity")
    externalId: Optional[None] = Field(None, alias="externalId")
    avgdsales: Optional[float] = Field(None, alias="avgdsales")
    avgdquantity: Optional[float] = Field(None, alias="avgdquantity")
    pstorage: Optional[bool] = Field(None, alias="pstorage")


class NewYearStatus(BaseModel):
    title: Optional[str] = Field(None, alias="title")
    color: Optional[str] = Field(None, alias="color")
    value: Optional[str] = Field(None, alias="value")


class Product(BaseModel):
    productId: Optional[int] = Field(None, alias="productId")
    category: Optional[str] = Field(None, alias="category")
    rating: Optional[str] = Field(None, alias="rating")
    status: Optional[Status] = Field(None, alias="status")
    moderationStatus: Optional[ModerationStatus] = Field(
        None, alias="moderationStatus"
    )
    commission: Optional[None] = Field(None, alias="commission")
    commissionDto: Optional[CommissionDto] = Field(None, alias="commissionDto")
    skuList: Optional[List[Sku]] = Field(None, alias="skuList")
    skuTitle: Optional[str] = Field(None, alias="skuTitle")
    image: Optional[str] = Field(None, alias="image")
    previewImg: Optional[str] = Field(None, alias="previewImg")
    title: Optional[str] = Field(None, alias="title")
    quantityActive: Optional[int] = Field(None, alias="quantityActive")
    quantityFbs: Optional[int] = Field(None, alias="quantityFbs")
    quantityAdditional: Optional[int] = Field(None, alias="quantityAdditional")
    quantityOnPhotoStudio: Optional[int] = Field(
        None, alias="quantityOnPhotoStudio"
    )
    quantityCreated: Optional[int] = Field(None, alias="quantityCreated")
    quantitySold: Optional[int] = Field(None, alias="quantitySold")
    quantityReturned: Optional[int] = Field(None, alias="quantityReturned")
    quantityDefected: Optional[int] = Field(None, alias="quantityDefected")
    quantityPending: Optional[int] = Field(None, alias="quantityPending")
    returnedPercentage: Optional[float] = Field(None, alias="returnedPercentage")
    newYearStatus: Optional[NewYearStatus] = Field(None, alias="newYearStatus")
    price: Optional[float] = Field(None, alias="price")
    clicks: Optional[None] = Field(None, alias="clicks")
    viewers: Optional[int] = Field(None, alias="viewers")
    conversion: Optional[float] = Field(None, alias="conversion")
    roi: Optional[str] = Field(None, alias="roi")
    rankInfo: Optional[RankInfo] = Field(None, alias="rankInfo")
    blockReason: Optional[None] = Field(None, alias="blockReason")
    dateModerated: Optional[None] = Field(None, alias="dateModerated")
    skusHasAllRequiredFilters: Optional[bool] = Field(
        None, alias="skusHasAllRequiredFilters"
    )
    pstorage: Optional[bool] = Field(None, alias="pstorage")


class Model(BaseModel):
    productList: List[Product] = Field(None, alias="productList")
    totalProductsAmount: Optional[int] = Field(None, alias="totalProductsAmount")


async def fetch_inventory_data_ke(shop_id: str, token: str = ""):

    url = f"https://api.business.kazanexpress.ru/api/seller/shop/{shop_id}/product/getProducts?searchQuery=&filter=all&sortBy=id&order=descending&size=10000&page=0"

    headers = {
        'authority': 'api.business.kazanexpress.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6,fr;q=0.5,pl;q=0.4,vi;q=0.3,de;q=0.2,sv;q=0.1',
        'authorization': f'Bearer RE46_R7D8SSeswlPtsAore0-Z1w',
        'origin': 'https://business.kazanexpress.ru',
        'referer': 'https://business.kazanexpress.ru/',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        print(f"Status code: {response.status_code}")
        return orjson.loads(response.text)


def flattering_json_file(source_data) -> List[Dict[str, Any]]:
    flat_list = []
    product_obj = Model(**source_data)
    for index, product in enumerate(source_data['productList']):
#         print(index)
        base_data = {
            'store_id': '24617',
            'store_name': 'Store_UZUM',
            'store_total_ProductsAmount': source_data['totalProductsAmount'],
            'product_id': product_obj.productList[index].productId,
            'category': product_obj.productList[index].category,
            'rating': product_obj.productList[index].rating,
            'status_id': product_obj.productList[index].status.id,
            'status_title': product_obj.productList[index].status.title,
            'status_value': product_obj.productList[index].status.value,
            'staus_description': product_obj.productList[index].status.description,
            'status_additional': product_obj.productList[index].status.additional,
            'moderationStatus_title': product_obj.productList[index].moderationStatus.title,
            'moderationStatus_value': product_obj.productList[index].moderationStatus.value,
            'commissionDto_minCommission': product_obj.productList[index].commissionDto.minCommission,
            'commissionDto_maxCommission': product_obj.productList[index].commissionDto.maxCommission,
            'clicks': product_obj.productList[index].clicks,
            'views': product_obj.productList[index].viewers,
            'conversion': product_obj.productList[index].viewers,
            'roi': product_obj.productList[index].roi,
            'dateUpdated': product_obj.productList[index].rankInfo.dateUpdated,
        }
        for sku in product_obj.productList[index].skuList:
            flat_product = base_data.copy()
            flat_product.update({
                'skuFullTitle': sku.skuFullTitle,
                'productTitle': sku.productTitle,
                'skuId': sku.skuId,
                'quantityCreated': sku.quantityCreated,
                'quantityReturned': sku.quantityReturned,
                'quantityDefected': sku.quantityDefected,
                'quantityPending': sku.quantityPending,
                'returnedPercentage':  sku.returnedPercentage,
                'barcode': sku.barcode,
                'archived': sku.archived,
                'commission': sku.commission,
                'characteristics': sku.characteristics,
                'purchasePrice': sku.purchasePrice,
                'price': sku.price,
                'rankInfo_rank': sku.rankInfo.rank,
                'rankInfo_dateUpdated': sku.rankInfo.dateUpdated,
                'discountPrice': sku.discountPrice,
                'article': sku.article,
                'turnover': sku.turnover,
                'paidStorageCost': sku.paidStorageCost,
                'length': sku.length,
                'width': sku.width,
                'height': sku.height,
                'paidStorageVolume': sku.paidStorageVolume,
                'paidStorageQuantity': sku.paidStorageQuantity,
                'externalId': sku.externalId,
                'avgdsales': sku.avgdsales,
                'avgdquantity': sku.avgdquantity,
                'pstorage': sku.pstorage
            })
            flat_list.append(flat_product)
    return flat_list

async def fetch_all_shops(shop_ids):
    tasks = []
    for shop_id in shop_ids:
        tasks.append(fetch_inventory_data_ke(shop_id))
    results = await asyncio.gather(*tasks)
    return results


async def main_ke():
    start_time = time.time()
    shop_ids = ["30745", "20509"]
    data = await fetch_all_shops(shop_ids)
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
    return data

async def load_data_inside_database() -> None:
    flat_json = json.dumps(flat_list)

    flat_listjob_config = bigquery.LoadJobConfig()
    job_config = LoadJobConfig(
        source_format=SourceFormat.NEWLINE_DELIMITED_JSON,
        autodetect=True,
    )
    # table = dataset.table(table_id)

    job = client.load_table_from_json(flat_list, table, job_config = job_config)
    
    await job.result()