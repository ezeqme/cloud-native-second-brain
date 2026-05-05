---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Takashi Norimatsu", "Hitachi", "Thomas Darimont", "Codecentric AG"]
sched_url: https://kccnceu2024.sched.com/event/1YhiQ/the-leading-edge-of-authn-and-authz-by-keycloak-takashi-norimatsu-hitachi-thomas-darimont-codecentric-ag
youtube_search_url: https://www.youtube.com/results?search_query=The+Leading+Edge+of+AuthN+and+AuthZ+by+Keycloak+CNCF+KubeCon+2024
slides: []
status: parsed
---

# The Leading Edge of AuthN and AuthZ by Keycloak - Takashi Norimatsu, Hitachi & Thomas Darimont, Codecentric AG

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Takashi Norimatsu, Hitachi, Thomas Darimont, Codecentric AG
- Schedule: https://kccnceu2024.sched.com/event/1YhiQ/the-leading-edge-of-authn-and-authz-by-keycloak-takashi-norimatsu-hitachi-thomas-darimont-codecentric-ag
- Busca YouTube: https://www.youtube.com/results?search_query=The+Leading+Edge+of+AuthN+and+AuthZ+by+Keycloak+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre The Leading Edge of AuthN and AuthZ by Keycloak.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YhiQ/the-leading-edge-of-authn-and-authz-by-keycloak-takashi-norimatsu-hitachi-thomas-darimont-codecentric-ag
- YouTube search: https://www.youtube.com/results?search_query=The+Leading+Edge+of+AuthN+and+AuthZ+by+Keycloak+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=DMwPjsG4wIM
- YouTube title: The Leading Edge of AuthN and AuthZ by Keycloak - Takashi Norimatsu & Thomas Darimont
- Match score: 0.814
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/the-leading-edge-of-authn-and-authz-by-keycloak/DMwPjsG4wIM.txt
- Transcript chars: 27339
- Keywords: access, policy, client, application, authentication, policies, password, called, request, identity, authorization, device, instance, whether, support, following, allows, information

### Resumo baseado na transcript

hello everybody uh thank you for joining this talk uh this talk consist of two part in the first part I would like to talk about the security mainly security features that latest KY CL supported also try to support in the future then in the second part the Thomas will demonstrate the potential integration of ke with open policy agent so let's start my part okay uh before my talk let me introduce myself to you briefly my name is Takashi noru the key Mainer and also working atachi

### Excerpt da transcript

hello everybody uh thank you for joining this talk uh this talk consist of two part in the first part I would like to talk about the security mainly security features that latest KY CL supported also try to support in the future then in the second part the Thomas will demonstrate the potential integration of ke with open policy agent so let's start my part okay uh before my talk let me introduce myself to you briefly my name is Takashi noru the key Mainer and also working atachi limited Japan I have been contributing mainly C fatures to K gr for example the WCC web cation API support and some the supporting or complying with the RFC standard documentation specification and also all to based apt profile support to keyr as follows uh as you may know the key clock is identity and access management open source software also the cncf incubating project since since last year Theo provides the each each Futures and also supporting the sever open standard for authentication and authorization and in my part I would like to talk about the following items topics the pass keys or 2.1 and oid for VCI so let's move on to the first topic Pass key uh pass Keys allows us to auate ourself uh without using password instead of using password using the cryptographic key then there are two types of Pass Key the sync Pass Key and device bound Pass Key also two types of authentication the cross device authentication and same device authentication so the K 23 starts supporting these passy authentication features however the from technological point of view the py authentication is the same the LLY the same as web a authentication that key had already uh start supported since the version n but nowadays the it seems that P key authentication are common now because the p key authentication are supported by the maure uh sever measure platforms as follows so just as just mentioned before the there are two type of Pass Key sync Pass Key and device B Pass key uh the device bound Pass key is uh bound with your the own device single device why the single Pass key is bound with your major IDP identity providers the user account for example the Google account and app ID so therefore the youth can share past SLE Pass Key among your own s devices by using the cloud services synchronization for example the Google password manager and up iCloud keychain also as just mentioned before there are two type of Authentication same device ofation and cross device ofation and let's assume that you use yo
