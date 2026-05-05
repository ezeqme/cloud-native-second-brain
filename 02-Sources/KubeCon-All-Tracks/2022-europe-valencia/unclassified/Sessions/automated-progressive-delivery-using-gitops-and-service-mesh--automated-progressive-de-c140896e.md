---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Unclassified"
themes: ["Networking", "GitOps Delivery"]
speakers: ["Yasen Simeonov", "Henrik Blixt", "Intuit"]
sched_url: https://kccnceu2022.sched.com/event/ytng/automated-progressive-delivery-using-gitops-and-service-mesh-yasen-simeonov-henrik-blixt-intuit
youtube_search_url: https://www.youtube.com/results?search_query=Automated+Progressive+Delivery+Using+GitOps+and+Service+Mesh+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Automated Progressive Delivery Using GitOps and Service Mesh - Yasen Simeonov & Henrik Blixt, Intuit

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Unclassified]]
- Temas: [[Networking]], [[GitOps Delivery]]
- País/cidade: Spain / Valencia
- Speakers: Yasen Simeonov, Henrik Blixt, Intuit
- Schedule: https://kccnceu2022.sched.com/event/ytng/automated-progressive-delivery-using-gitops-and-service-mesh-yasen-simeonov-henrik-blixt-intuit
- Busca YouTube: https://www.youtube.com/results?search_query=Automated+Progressive+Delivery+Using+GitOps+and+Service+Mesh+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Automated Progressive Delivery Using GitOps and Service Mesh.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytng/automated-progressive-delivery-using-gitops-and-service-mesh-yasen-simeonov-henrik-blixt-intuit
- YouTube search: https://www.youtube.com/results?search_query=Automated+Progressive+Delivery+Using+GitOps+and+Service+Mesh+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5Ko-CnP2qhA
- YouTube title: Automated Progressive Delivery Using GitOps and Service Mesh - Yasen Simeonov & Henrik Blixt, Intuit
- Match score: 0.854
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/automated-progressive-delivery-using-gitops-and-service-mesh/5Ko-CnP2qhA.txt
- Transcript chars: 27963
- Keywords: traffic, mesh, argo, version, actually, progressive, delivery, gateway, deploy, cluster, clusters, figure, analysis, probably, application, experience, looking, basically

### Resumo baseado na transcript

whoa it's 5 25 so many people thank you for joining us i hope we will make your time here worth it i promise we will not say anything we'll just share our experience my name is jason simeonov and i'm product manager at intuit in the looking after the developer experience and i'm more focused on the service mentioned api gateway and yeah henrik hi everyone my name is henrik blixt i'm also a product manager at intuit and i'm also one of the the argo maintainers so we're

### Excerpt da transcript

whoa it's 5 25 so many people thank you for joining us i hope we will make your time here worth it i promise we will not say anything we'll just share our experience my name is jason simeonov and i'm product manager at intuit in the looking after the developer experience and i'm more focused on the service mentioned api gateway and yeah henrik hi everyone my name is henrik blixt i'm also a product manager at intuit and i'm also one of the the argo maintainers so we're quickly today going to talk a little bit about how we use service mesh and how it looks at intuit i'm going to talk a bit about progressive delivery why we use it how we use it and then i'm going to talk about how well they work together or how well they didn't work together and we kind of what we experienced and realized as we tried to use these together a little bit look into the future what we think is coming next what are the big focus areas for us and then we're going to round off with jason doing a live demo so very quickly but into it since we're in europe not too many of you probably know who we are because we have 95 of our business in in the us but we're one of the leading u.s fintech companies we have roughly 10 billion dollars in in revenue what you probably know is more for if you knew is that our the argo project came out of intuit where it came out of a startup that we acquired and then we later donated argo to the cncf we're big supporters of open source not just argo but a number of other projects that we contribute to that we use basically if it's in this cnc but you've probably all seen that massive map right if it's on that map we pretty much use it and we contribute to many of them uh as well okay my turn yeah before going to this slide i just out of curiosity how many of you are here because of the service mesh part can how great yeah great and how many because of the progressive delivery in targo whoa great okay excellent i think this slides uh shows our scale and it is important for the service mesh part because you can see that we have around more than 230 uh kubernetes clusters and the service measure that i'm going to talk about in a moment stretches across all those clusters so we have one single mesh across all those clusters rest is like uh dynamic so our uh not count is growing depending on the period we have some peak periods where the count grows and some quad period when the car goes down uh yeah so we have more than seven million pots running in our infrastr
