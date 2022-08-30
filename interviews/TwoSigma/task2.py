def getResults(bids, totalShares):
    # Give all the shares to the one bidder.
    if len(bids) == 1:
        return []
    
    # Sort bids by price in descending order and then sort by timestamp if multiple bids have the same price.
    bids.sort(key=lambda x:(-x[2], x[3]))

    bidId = 1
    while totalShares > 0 and bidId < len(bids):
        if bids[bidId - 1][2] > bids[bidId][2]:
            totalShares = max(0, totalShares - bids[bidId - 1][1])
            if totalShares > 0:
                bidId += 1
        # Multiple bidders with the same price
        else:
            price = bids[bidId - 1][2]
            numPeopleSamePrice = 2
            numSharesSamePrice = bids[bidId - 1][1] + bids[bidId][1]
            i = bidId + 1
            # Get the group of bidders with the same price.
            while i < len(bids):
                if bids[i][2] != price:
                    break
                
                numPeopleSamePrice += 1
                numSharesSamePrice += bids[i][1]
                i += 1
            
            # If shares is less than total, then we give all the bidders with the same price shares.
            if numSharesSamePrice < totalShares:
                totalShares -= numSharesSamePrice
                bidId = i
            else:
                # If there's more people than shares, then some people with the same price won't get shares.
                if numPeopleSamePrice > totalShares:
                    bidId += (totalShares - 1)
                else:
                    bidId = i
                    break

        biddersWithNoShares = []
        for i in range(bidId, len(bids)):
            biddersWithNoShares.append(bids[i][0])

        biddersWithNoShares.sort()
        return biddersWithNoShares
