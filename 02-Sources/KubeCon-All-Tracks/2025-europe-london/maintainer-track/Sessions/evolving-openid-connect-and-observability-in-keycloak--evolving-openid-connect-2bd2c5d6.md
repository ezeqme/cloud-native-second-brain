---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Observability", "Community Governance"]
speakers: ["Ryan Emerson", "Red Hat", "Takashi Norimatsu", "Hitachi"]
sched_url: https://kccnceu2025.sched.com/event/1td1c/evolving-openid-connect-and-observability-in-keycloak-ryan-emerson-red-hat-takashi-norimatsu-hitachi
youtube_search_url: https://www.youtube.com/results?search_query=Evolving+OpenID+Connect+and+Observability+in+Keycloak+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Evolving OpenID Connect and Observability in Keycloak - Ryan Emerson, Red Hat & Takashi Norimatsu, Hitachi

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Ryan Emerson, Red Hat, Takashi Norimatsu, Hitachi
- Schedule: https://kccnceu2025.sched.com/event/1td1c/evolving-openid-connect-and-observability-in-keycloak-ryan-emerson-red-hat-takashi-norimatsu-hitachi
- Busca YouTube: https://www.youtube.com/results?search_query=Evolving+OpenID+Connect+and+Observability+in+Keycloak+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Evolving OpenID Connect and Observability in Keycloak.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1td1c/evolving-openid-connect-and-observability-in-keycloak-ryan-emerson-red-hat-takashi-norimatsu-hitachi
- YouTube search: https://www.youtube.com/results?search_query=Evolving+OpenID+Connect+and+Observability+in+Keycloak+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=bC4xbBJs0CA
- YouTube title: Evolving OpenID Connect and Observability in Keycloak - Ryan Emerson & Takashi Norimatsu
- Match score: 0.854
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/evolving-openid-connect-and-observability-in-keycloak/bC4xbBJs0CA.txt
- Transcript chars: 19602
- Keywords: metrics, access, keycloak, application, requests, request, specification, wallet, issuer, provide, database, milliseconds, security, support, therefore, hopefully, recent, called

### Resumo baseado na transcript

So hello everyone and we are very happy to have today that talked about the key cro and thank you for joining this the presentation. The first part of this talk is uh about introducing to you the recent tick clock update about security future support. So, in the past of this talk, I just mentioned before I'd like to talk about the key recent security at a future updates. Then so the OC not only do the contribution to the newly supporting security specification to tro but also do the contribution to the define the tro already supported security futures. In this talk the I would like to pick up two security specification that the relatively the recent Tro the supported RFC 9449 O2 demonstrating proof of position uh called DOP and open ID for verifiable querial issuance called OD for VCI And the depot enables you to prevent the misuse of a stolen access token. So, in order to prevent such security features, the depot uh might can be used.

### Excerpt da transcript

So hello everyone and we are very happy to have today that talked about the key cro and thank you for joining this the presentation. H this uh presentation consists of the two part. The first part of this talk is uh about introducing to you the recent tick clock update about security future support. While the second half of this talk we would like to introduce to you the key recent updates on observability and give some demonstration about that. So in the part of this talk I would like to talk about the tro recent update on security futures. Uh before my talk let me introduce myself to you briefly. My name is Takashin Matsu and working for Hitachi limited Japan and I am also the keyro maintainer. In this talk in this talk I would like to introduce to you the two trog special interest group the community activity uh trog oc and tro st reliability engineers s the objective of of oc is to support o thec and it related cert specification support to kro to make trog more secure while the objective of s is to improve the lives of the people like you learning grog and operating grog.

So the both hik has its own uh github repository and also cncf channel. Therefore, if you are interested in the the activity of Zo, please access to the CNCF swag channel is an appropriate place for you. So, in the past of this talk, I just mentioned before I'd like to talk about the key recent security at a future updates. And uh the this slide shows the recent contributions by the community OC. And uh futures marked with the test tube means that uh those futures are rated as experimental or preview future not official future. uh while the items marked with the check box uh means that those futures are treated as official officially supported future. Then so the OC not only do the contribution to the newly supporting security specification to tro but also do the contribution to the define the tro already supported security futures. And this slide shows an example of such the contribution for refinement. In this talk the I would like to pick up two security specification that the relatively the recent Tro the supported RFC 9449 O2 demonstrating proof of position uh called DOP and open ID for verifiable querial issuance called OD for VCI And the depot enables you to prevent the misuse of a stolen access token.

Erh, as you might know, the O2 uh specification RFC 6950 states that an access to an access token is treated as bearer token which means that everyone holding an access token
