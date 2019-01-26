def paging(data, all):
    import math
    # 每页多少条
    num = data.get("limit")
    # 第几页
    page = data.get("page")
    # 总数据条数
    total = len(all)
    if not page:
        page = 1
    num = int(num)
    page = int(page)
    # 共多少页
    pages = math.ceil(total / num)
    # 起始条数
    start = num * (page - 1)
    end = num * page
    return total, pages, start, end
