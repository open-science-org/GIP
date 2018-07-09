# Generalized Idea Protocol (GIP) 
previously called **Interplanetary Idea System (IPIS)**

### What is an Idea?
Idea is an entity which generates new information at the time of its creation. It can be a publication, book, website, blog, data, legal document, or anything physical/virtual object or concept.
![Idea](idea.png)

### What is GIP?
GIP is a protocol that defines an idea and the relationship between two or more ideas. The relationship between two ideas will define:
- the association strength between the ideas
- the agreement between the owners of the ideas 
- the idea flow between them
- the value flow between them. If an idea B which is dependent on idea A generates value of $100, how is this value shared to the idea A? and how does the value shared to idea A (let's say $5) is shared to the ideas it was based upon? In other words, how does the value flow back?
![Relationship Between Two Ideas](relationship_ideas.png)


With GIP, each unique idea can be identified and its evolution over the time can be tracked. In addition, it will give us a framework to evaluate the relationship between two different ideas. One way of modeling GIP would be by a directed acyclic graph (DAG) that grows over time. Each node of the DAG will be an GIP object representing a unique idea.  An GIP object will contain all the information required to represent a unique idea. If there is a publication or data (stored as an IPFS object) related to an idea, its GIP object will contain the cryptographic hash of the IPFS object. 

GIP will allow us to track the evolution of ideas over time as well as quantify the similarity of two ideas. The similarity score can be a hybrid of the market-driven score (decided by the scientific community via voting) and the algorithmic score generated from the GIP protocol. GIP will facilitate the efficient sharing of the ideas and prevent the community from reinventing wheels, thereby accelerating the pace of the scientific research. In addition, a good visualization of GIP objects will help the scientific community to identify the pain points of scientific research. Similarly, it can be used to find the optimal distribution of available resources (e.g. fund allocation) required in order to maximize scientific throughput. Loosely speaking, GIP will store the collective thought process of the whole scientific community.

### Mathematical Definition
Mathematically, GIP is a directed acyclic graph (DAG) that grown over time. Each node in GIP contains enough information to describe a unique idea I. The edge between two nodes representing ideas I1 and I2 will show the relationship (magnitude and direction of idea/information flow) between I1 and I2.

### Idea Flow
![Idea Flow](Idea_flow.png)
Idea I_0 cites Idea I_1, I_2, and I_3. Here the idea I_0 is borrowing some knowldge from the cited publications (its parent ideas), so the idea flows from I_1, I_3, and I_3 to I_0.

### Value Flow
![Value Flow](Value_flow.png)
The value (in form of OSO tokens) flows backward i.e. opposite to the idea flow.

## GIP v.0.0 (basic version)
*we will implement this first*

Each node of GIP will represent a publication and an edge will represent the direction of “idea flow”; the strength of relationship (or magnitude) is same for all idea pairs. This means first order “cost of idea” is same across the graph. However, it can be user dependent by design. For example, let’s say an entity publishes a publication A where publications B, C, D, & E are cited. In other words, the costs of idea of publications B, C, D, & E are equal for publication A. However, if the entity feels (and the reviewer agrees) that the publication A is more dependent on publications B & D, the entity can redistribute the costs of idea as (B, C, D, E) = (5, 1, 10, 1).

