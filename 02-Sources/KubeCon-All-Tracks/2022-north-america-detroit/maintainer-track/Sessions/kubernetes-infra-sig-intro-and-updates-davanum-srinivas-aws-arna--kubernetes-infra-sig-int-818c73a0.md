---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: []
sched_url: https://kccncna2022.sched.com/event/182OG/kubernetes-infra-sig-intro-and-updates-davanum-srinivas-aws-arnaud-meukam-independent-benjamin-elder-google
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes%C2%A0Infra%C2%A0SIG%3A%C2%A0Intro%C2%A0And%C2%A0Updates%C2%A0-%C2%A0Davanum%C2%A0Srinivas%2C+AWS%3B+Arnaud%C2%A0Meukam%2C+Independent%3B%C2%A0Benjamin%C2%A0Elder%2C%C2%A0Google+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Kubernetes Infra SIG: Intro And Updates - Davanum Srinivas, AWS; Arnaud Meukam, Independent; Benjamin Elder, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: N/A
- Schedule: https://kccncna2022.sched.com/event/182OG/kubernetes-infra-sig-intro-and-updates-davanum-srinivas-aws-arnaud-meukam-independent-benjamin-elder-google
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes%C2%A0Infra%C2%A0SIG%3A%C2%A0Intro%C2%A0And%C2%A0Updates%C2%A0-%C2%A0Davanum%C2%A0Srinivas%2C+AWS%3B+Arnaud%C2%A0Meukam%2C+Independent%3B%C2%A0Benjamin%C2%A0Elder%2C%C2%A0Google+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Kubernetes Infra SIG: Intro And Updates - Davanum Srinivas, AWS; Arnaud Meukam, Independent; Benjamin Elder, Google.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182OG/kubernetes-infra-sig-intro-and-updates-davanum-srinivas-aws-arnaud-meukam-independent-benjamin-elder-google
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes%C2%A0Infra%C2%A0SIG%3A%C2%A0Intro%C2%A0And%C2%A0Updates%C2%A0-%C2%A0Davanum%C2%A0Srinivas%2C+AWS%3B+Arnaud%C2%A0Meukam%2C+Independent%3B%C2%A0Benjamin%C2%A0Elder%2C%C2%A0Google+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=mJAC4asDCOw
- YouTube title: Kubernetes Infra SIG: Intro And Updates - Davanum Srinivas, Arnaud Meukam, Benjamin Elder
- Match score: 0.96
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/kubernetes-infra-sig-intro-and-updates-davanum-srinivas-aws-arnaud-meu/mJAC4asDCOw.txt
- Transcript chars: 31278
- Keywords: basically, google, infrastructure, traffic, running, registry, cost, amazon, actually, container, provider, working, inside, resources, images, question, trying, credits

### Resumo baseado na transcript

hi everyone and welcome to the communities Andra uh this is mostly an intro and update of the S so this is the first time we doing this because historically we were a working group so we didn't have the possibility to make an intro and we became a see October of last year which means in term of community we have authority to basically provide information about what we're doing so welcome to everyone in this call um we will start okay let's go okay so my name is migrating these things out of Google what we're talking about is migrating them either from some special internal infrastructure or from google.com organization gcp projects to kubernetes doio gcp projects we are still almost entirely on gcp but we are moving things to where it's it possible for other vendors and the community to participate and controlling how this works cost-wise how we distribute things latency whatever we don't need a single vendor solution kubernetes is all about hybrid Cloud how can we safely offload these things um so it's we've moved to artifact registry redesign Google container registry and we are using Regional instances ourselves in 20 regions around the globe and the community controls all of this it runs also with three come back to that so we have gcp infrastructure in place the kubernetes project has been about one to two weeks away from reaching the exhaustion of our credits running...

### Excerpt da transcript

hi everyone and welcome to the communities Andra uh this is mostly an intro and update of the S so this is the first time we doing this because historically we were a working group so we didn't have the possibility to make an intro and we became a see October of last year which means in term of community we have authority to basically provide information about what we're doing so welcome to everyone in this call um we will start okay let's go okay so my name is ano mam I'm a senior software engineer I work for uh let's say specialized company in kuity distribution I will be with Benjamin Elder a Senor engineer from Google dims I think anyone know dims is actually in a different meeting in my B it so we're going to be the two people doing the presentation we uh actually just came from the governing board meeting talking to them about the uh Kate and for situation and dims is still there representing us should we go there it's not open invite sorry fortunately most comp most company have people over there to to talk about the different KRA subject so what is s inra we are a working group specialized in basically have a full ownership of the community infrastructure and I want to put things in context cuberes is a seveny year project and they initially start inside Google using Google infrastructure and over time and over the different step of the project there were there were conversation about basically make the community aware of the infrastructure they running and gave the community full ownership that's why we start as a working group have conversation about how we transfer all the resources and all the asset of the project from the go infrastructure to a community own infrastructure and that's where we start as a working group so the main responsibility of the see is to be responsible for first and that's like the first step of the this group be responsible of the successful migration from Google infrastructure to the community own and Community own in the sense that this is fully controlled by the community and support by cntf and basically no overall with people from Google uh we also basically we have authority to basically establish policy about where we want to R the future based on different aspect of the environment might be ethical might be a soci a social issue so we trying to basically get consensus about the decision Rel to infrastructure so we have different policy around running the cuber infrastructure we're also trying to provide report a
