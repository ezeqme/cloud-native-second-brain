---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Customizing + Extending Kubernetes"
themes: ["Kubernetes Core"]
speakers: ["Alex Jones", "Anaïs Urlichs", "Civo"]
sched_url: https://kccncna2021.sched.com/event/lV3z/how-we-built-a-cloud-on-k3s-the-learnings-of-growing-up-fast-alex-jones-anais-urlichs-civo
youtube_search_url: https://www.youtube.com/results?search_query=How+We+Built+a+Cloud+On+K3s%3A+The+Learnings+Of+Growing+Up+Fast+CNCF+KubeCon+2021
slides: []
status: parsed
---

# How We Built a Cloud On K3s: The Learnings Of Growing Up Fast - Alex Jones & Anaïs Urlichs, Civo

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Alex Jones, Anaïs Urlichs, Civo
- Schedule: https://kccncna2021.sched.com/event/lV3z/how-we-built-a-cloud-on-k3s-the-learnings-of-growing-up-fast-alex-jones-anais-urlichs-civo
- Busca YouTube: https://www.youtube.com/results?search_query=How+We+Built+a+Cloud+On+K3s%3A+The+Learnings+Of+Growing+Up+Fast+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre How We Built a Cloud On K3s: The Learnings Of Growing Up Fast.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV3z/how-we-built-a-cloud-on-k3s-the-learnings-of-growing-up-fast-alex-jones-anais-urlichs-civo
- YouTube search: https://www.youtube.com/results?search_query=How+We+Built+a+Cloud+On+K3s%3A+The+Learnings+Of+Growing+Up+Fast+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vDL-rCDp0oM
- YouTube title: How We Built a Cloud On K3s: The Learnings Of Growing Up Fast - Alex Jones & Anaïs Urlichs, Civo
- Match score: 0.88
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/how-we-built-a-cloud-on-k3s-the-learnings-of-growing-up-fast/vDL-rCDp0oM.txt
- Transcript chars: 14248
- Keywords: clusters, cluster, having, tenant, within, meaning, compute, actually, infrastructure, ability, provider, extremely, single, supercluster, virtual, machine, culture, across

### Resumo baseado na transcript

hello there and thank you so much for joining us here at our cubecon talk how we will declare on k3s the learnings of growing up fast my name is anais orlis i'm a zed reliability engineer at sibo before joining civil i worked for several years as developer advocate first in the blockchain space and then transitioned into devops i also started a challenge called 100 days of kubernetes where we aim to learn something new related to cubanitas across 100 days if you are curious you can find

### Excerpt da transcript

hello there and thank you so much for joining us here at our cubecon talk how we will declare on k3s the learnings of growing up fast my name is anais orlis i'm a zed reliability engineer at sibo before joining civil i worked for several years as developer advocate first in the blockchain space and then transitioned into devops i also started a challenge called 100 days of kubernetes where we aim to learn something new related to cubanitas across 100 days if you are curious you can find more resources on my twitter linked on the slide hi there i'm alex jones i'm the principal engineer here at sivo i'm also a technical advisory group technical lead for app delivery within the cncf i've worked companies such as microsoft beat sky b jp morgan american express and many more and you can always reach me on alex jones ax at twitter if you want to chat so what is sievo what are we actually basing our experience that we share with you here in this talk on xero is our managed kubernetes provider meaning you can spin up kubernetes clusters in 90 seconds or less we are highly community focused and community driven meaning a lot of our offering is based on community input also our platform provides several different options to allow for community feedback and community created resources to contribute and help us grow the platform additionally sivo is based on k3s which is a separate kubernetes distribution that allows us a lot of the features that we will talk about throughout this presentation so why is there a need for yet another managed kubernetes provider well first of all the market is growing more and more people want to use kubernetes either for their personal projects or for their company's needs so in itself people want to be able to use cubans as quickly as possible with little hassle and without having to read any books on how to actually do it secondly sivo is based on k3s there is not yet a managed kubernetes provider that is based on k3s we will dive into more detail into what k3s actually is in a second and lastly there is a need for a cloud-native kubernetes service provider sivo is cloud native first a lot of the cncf projects that you will hear about throughout this kubecon are actually integrated with you can spin them up when you spin up a kubernetes cluster alongside it so you don't have to dig through endless documentation but you're up and running quickly with the tools and platforms that you want to use on top of your kubernetes cluster so what
