## How will new researchers acquire OSO tokens?
New resarchers will acquire token:
1) by purchasing from an exchange or any USD/OSO conversion platform
2) by adding value to the ecosystem (e.g. by reviewing the papers, by submitting the errors, by curating the datasets)
3) as a gift from senior researchers (e.g. PhD advisors)

## What would happen if a biotech/pharma buys a large amount of OSO tokens, can they game the system this way?


## Is there a limit to the amount of OSO tokens 1 entity can hold in a wallet?
No


## Will researchers be able to use OSO tokens to fund their own research or research activities?
Yes

### If OSO is traded for outside funds, it breaks the closed loop system of the utility token

  See this [thread](https://www.reddit.com/r/BATProject/comments/7q1iev/do_advertisers_need_to_buy_bat_in_order_to_be/?st=JI2DLH19&sh=7c5ecbb71) on reddit.  Specifically the comment from cryptocurrentsee.
  "One thing I can't square in my mind..."


## How is reputation tracked in the system?
First, we have to define reputation scores.
I am in favor of multidimensional reputation scores (a vector) where each dimension will quanity some facet of reputation. Also, there can be multiple different reputation scores (e.g. overall reputation scores of the plaform and reputation scores for each sub-network).

**Vanilla design:**

*Start*      
Overall Reputation score of an entity: R = (R1, R2, R3)     
 where, R1 = f1(Txs), R2 = f2(Txs), R3 = f3(Txs)

 Txs = a list of activities of the entity on the platform or outside    
 f1, f2, f3 = functions that govern the calculation of reputation scores   

 *Update Rule*     
 Rn(t+T) = Rn(t) + fn(Txs within time period T) (assuming reputation is updated with interval of T)


