---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Alexander Schwartz", "IBM", "Sebastian Łaskawiec", "Defense Unicorns"]
sched_url: https://kccnceu2026.sched.com/event/2EF6o/sovereign-identities-for-your-cloud-native-architecture-with-keycloak-alexander-schwartz-ibm-sebastian-laskawiec-defense-unicorns
youtube_search_url: https://www.youtube.com/results?search_query=Sovereign+Identities+for+Your+Cloud+Native+Architecture+With+Keycloak+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Sovereign Identities for Your Cloud Native Architecture With Keycloak - Alexander Schwartz, IBM & Sebastian Łaskawiec, Defense Unicorns

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Alexander Schwartz, IBM, Sebastian Łaskawiec, Defense Unicorns
- Schedule: https://kccnceu2026.sched.com/event/2EF6o/sovereign-identities-for-your-cloud-native-architecture-with-keycloak-alexander-schwartz-ibm-sebastian-laskawiec-defense-unicorns
- Busca YouTube: https://www.youtube.com/results?search_query=Sovereign+Identities+for+Your+Cloud+Native+Architecture+With+Keycloak+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Sovereign Identities for Your Cloud Native Architecture With Keycloak.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF6o/sovereign-identities-for-your-cloud-native-architecture-with-keycloak-alexander-schwartz-ibm-sebastian-laskawiec-defense-unicorns
- YouTube search: https://www.youtube.com/results?search_query=Sovereign+Identities+for+Your+Cloud+Native+Architecture+With+Keycloak+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7q4oTEfrz1o
- YouTube title: Sovereign Identities for Your Cloud Native Architecture... Alexander Schwartz & Sebastian Łaskawiec
- Match score: 0.821
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/sovereign-identities-for-your-cloud-native-architecture-with-keycloak/7q4oTEfrz1o.txt
- Transcript chars: 23525
- Keywords: client, keycloak, application, credentials, secret, tokens, authentication, account, identity, supported, basically, around, access, connect, exchange, authorization, infrastructure, single

### Resumo baseado na transcript

So, it's uh about time that we start sovereign identities uh for your cloud native architecture with Keycloak. And let's get well deep into um Kubernetes infrastructure and keycloak. Um logs um originally we put them on the console and the file on sys log but with the general release we added also support for logs the same for support for metrics that was also in the January release um and and yeah and dashboards they also been around since last year. Currently we ship some Graphana dashboards that then capture a single pane of glass for your service level objectives around key so that you can measure like how good is my performance around logging in. So, um, if you're running on Kubernetes, there's something called a service account token that you can leverage. So during today's demo we'll focus on confidential clients which means client needs to authenticate in keycloak in order to get a token.

### Excerpt da transcript

them in. All right. So, it's uh about time that we start sovereign identities uh for your cloud native architecture with Keycloak. Welcome to this talk here at CubeCon. My name is Alexander Schwarz. I'm one of the key maintainers. >> My name is Sebastian Wascavis. I work for Defense Unicorns. >> All right. And let's get well deep into um Kubernetes infrastructure and keycloak. So in the end it's all about this well epic quest of how to do single sign on correctly. You want to have one identity and you want to delegate resource access to selected services. And the thing that we use nowadays is mostly open ID connect. We want to have or credentials. You want to keep them secure. And when you then have a like your single sign on service as keylog at some place, uh it will take care of those credentials and then issue shortlived tokens. And well digital sovereignty starts and ends when you well when you then host things for your own. So when someone else can pull the plug to your identity system, you're probably not as sovereign as you want to be.

Also, um when it comes to road map and adding features, um with an opensource project like keycloak, you can probably steer the road map a bit. All right, so about that a little short introduction to keycloak. So you have users with some devices. You have keycloak and what you need to do for that you download a container um start it up and connect it to the database and then you have services. Um the users login with their credentials um be it username, password, pass keys whatever with keycloak. Um then they get tokens you they use these tokens to access the services and once they these services can then either check these tokens by themselves uh or they can um yeah verify the token with keycloak so we can they can have a call back and introspect the token with open ID connect they can maybe there are even more things that are not in the token that can be retrieved from such an endpoint when we use lightweight tokens here but that's another story. Then you have like a very sovereign setup with your identities running locally.

But then identity is also like an integration topic. Um you can integrate keycloak with it provides s and open money connect. You can integrate with other s and open money connect providers. You can also run in integrate with an LDub if you want to if you're an enterprise context. So in the end there are lots of connections uh happening and when you run it in your infrastructure you need to m
