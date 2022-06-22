from azure.identity import DefaultAzureCredential
from azure.mgmt.securityinsight import SecurityInsights
from azure.mgmt.securityinsight.models import Watchlist

def print_watchlists(sentinel:SecurityInsights, watchlists_rg:str, watchlists_ws:str):
    print(f"Listing all watchlists")
    watchlist:Watchlist
    for watchlist in sentinel.watchlists.list(resource_group_name=watchlists_rg, 
                                              workspace_name=watchlists_ws):
        print(f"\tListing entries from {watchlist.watchlist_alias}")
        for watchlist_item in sentinel.watchlist_items.list(resource_group_name=watchlists_rg, 
                                                            workspace_name=watchlists_ws, 
                                                            watchlist_alias=watchlist.watchlist_alias):
            print(f"\t\t{watchlist_item.items_key_value}")


def create_watchlist(sentinel:SecurityInsights, watchlists_rg:str, watchlists_ws:str, alias:str, display_name:str, data:str):

    watchlist = Watchlist(
        display_name=display_name,
        raw_content=data,
        provider="test",
        items_search_key="domain",
        source="testing",
        content_type="text/csv",
        number_of_lines_to_skip=0
    )
    
    sentinel.watchlists.create_or_update(
        resource_group_name=watchlists_rg,
        workspace_name=watchlists_ws,
        watchlist_alias=alias,
        watchlist=watchlist
    )


def main():
    
    watchlists_rg = 'sample-rg'
    watchlists_ws = 'sample-law'
    sub = '5e7f5f7b-f00e-4476-8a34-fbe2c5f9919a'
    cred = DefaultAzureCredential()
    sentinel = SecurityInsights(cred, sub)
    
    # Printing a watchlist
    print_watchlists(sentinel, watchlists_rg, watchlists_ws)

    # Creating a watchlist from scratch
    mock_data = """\
domain,category
phishing-website.com,phishing
ransomware-website.com,ransomware\
"""
    create_watchlist(sentinel, watchlists_rg, watchlists_ws, "bad-domains", "bad-domains", mock_data)

if __name__ == "__main__":
    main()

