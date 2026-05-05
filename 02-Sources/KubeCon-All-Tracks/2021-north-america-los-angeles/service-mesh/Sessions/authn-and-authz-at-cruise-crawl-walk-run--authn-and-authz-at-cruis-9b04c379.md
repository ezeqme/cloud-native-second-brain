---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Service Mesh"
themes: ["Networking"]
speakers: ["James Barclay", "Roman Porter", "Cruise"]
sched_url: https://kccncna2021.sched.com/event/lV6M/authn-and-authz-at-cruise-crawl-walk-run-james-barclay-roman-porter-cruise
youtube_search_url: https://www.youtube.com/results?search_query=AuthN+and+AuthZ+at+Cruise%3A+Crawl%2C+Walk%2C+Run+CNCF+KubeCon+2021
slides: []
status: parsed
---

# AuthN and AuthZ at Cruise: Crawl, Walk, Run - James Barclay & Roman Porter, Cruise

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Service Mesh]]
- Temas: [[Networking]]
- País/cidade: United States / Los Angeles
- Speakers: James Barclay, Roman Porter, Cruise
- Schedule: https://kccncna2021.sched.com/event/lV6M/authn-and-authz-at-cruise-crawl-walk-run-james-barclay-roman-porter-cruise
- Busca YouTube: https://www.youtube.com/results?search_query=AuthN+and+AuthZ+at+Cruise%3A+Crawl%2C+Walk%2C+Run+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre AuthN and AuthZ at Cruise: Crawl, Walk, Run.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV6M/authn-and-authz-at-cruise-crawl-walk-run-james-barclay-roman-porter-cruise
- YouTube search: https://www.youtube.com/results?search_query=AuthN+and+AuthZ+at+Cruise%3A+Crawl%2C+Walk%2C+Run+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=VrtlM7aOg2M
- YouTube title: AuthN and AuthZ at Cruise: Crawl, Walk, Run - James Barclay & Roman Porter, Cruise
- Match score: 0.782
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/authn-and-authz-at-cruise-crawl-walk-run/VrtlM7aOg2M.txt
- Transcript chars: 37417
- Keywords: request, authorization, actually, authentication, ingress, application, basically, mentioned, cluster, policy, identity, sidecar, tokens, permissions, libraries, envoy, security, access

### Resumo baseado na transcript

so my name is roman uh this is james and we both work at cruz cruz is a self-driving car technology company uh that works on a lot of different things but one of the main ones is trying to make a car drive by itself so today we're going to talk to you about um our journey through authentication and authorization and crews so james all right thanks roman um so just to sort of set the stage for the problem space that we'll be talking about here i'll sorry um and uh you know that's really hard to debug right because depending on the state of your headers at any given time this will fail or succeed so it's just not great um you know for us in security right that's great that we're providing all these libraries and side cars for folks but you know maintaining them is really hard you know at the end of the day we're kind of a security team we're not just like a development team uh but we have to not

### Excerpt da transcript

so my name is roman uh this is james and we both work at cruz cruz is a self-driving car technology company uh that works on a lot of different things but one of the main ones is trying to make a car drive by itself so today we're going to talk to you about um our journey through authentication and authorization and crews so james all right thanks roman um so just to sort of set the stage for the problem space that we'll be talking about here i'll just start by saying that cruz currently has about 2 000 employees of those employees approximately 1 500 of them are engineers and we've got about 150 services running at any given time the majority of our services are running in kubernetes with the mix of both my microservice and monolith architectures that span multiple clusters and most of the traffic that's passed around is http based as for storing and managing secrets we use hashicorp vault and we use a typical cloud-based identity provider for managing employee and contractor identity um and so when talking about authen and odyssey at cruz um we really have three different types of callers or clients that we have to take into consideration um and of the uh those callers are browser clients cli clients and service to service or application clients um and so i'll just start at the beginning you know this is more of like uh you know handling often an aussie at cruz to be honest during the early days was sort of like the wild west and this was really more you know our talk is called crawl walk run i'll say this is more of like the embryonic stage but it's worth mentioning nonetheless um so in this in this early stage you know we had for example engineers they're building services for example on top of our pas gke clusters and then in terms of how they handled authentication and authorization they're basically on their own the security team may have implemented policies or standards which required service owners to implement these controls but we didn't really have a whole lot in the way of tooling or standardization so i'll affectionately refer to these as the bad old days um and uh you know despite my initial impression this ban sounds absolutely nothing like kiss but nonetheless um i'll say that at this early stage we had authentication and authorization sprawl teams were handling often and obviously entirely differently for example you know one might be doing oidc with idp one and another might be doing oidc or saml with a different identity provider altog
