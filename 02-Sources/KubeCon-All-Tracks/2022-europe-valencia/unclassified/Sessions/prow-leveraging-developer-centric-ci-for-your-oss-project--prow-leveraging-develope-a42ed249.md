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
themes: ["Cloud Native"]
speakers: ["Nabarun Pal", "VMware", "Arsh Sharma", "Okteto"]
sched_url: https://kccnceu2022.sched.com/event/ytn6/prow-leveraging-developer-centric-ci-for-your-oss-project-nabarun-pal-vmware-arsh-sharma-okteto
youtube_search_url: https://www.youtube.com/results?search_query=Prow%21+Leveraging+Developer-Centric+CI+for+Your+OSS+Project%21+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Prow! Leveraging Developer-Centric CI for Your OSS Project! - Nabarun Pal, VMware & Arsh Sharma, Okteto

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Unclassified]]
- Temas: [[Cloud Native]]
- País/cidade: Spain / Valencia
- Speakers: Nabarun Pal, VMware, Arsh Sharma, Okteto
- Schedule: https://kccnceu2022.sched.com/event/ytn6/prow-leveraging-developer-centric-ci-for-your-oss-project-nabarun-pal-vmware-arsh-sharma-okteto
- Busca YouTube: https://www.youtube.com/results?search_query=Prow%21+Leveraging+Developer-Centric+CI+for+Your+OSS+Project%21+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Prow! Leveraging Developer-Centric CI for Your OSS Project!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytn6/prow-leveraging-developer-centric-ci-for-your-oss-project-nabarun-pal-vmware-arsh-sharma-okteto
- YouTube search: https://www.youtube.com/results?search_query=Prow%21+Leveraging+Developer-Centric+CI+for+Your+OSS+Project%21+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=sdU-3cqiJmg
- YouTube title: Prow! Leveraging Developer-Centric CI for Your OSS Project! - Nabarun Pal & Arsh Sharma
- Match score: 0.906
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/prow-leveraging-developer-centric-ci-for-your-oss-project/sdU-3cqiJmg.txt
- Transcript chars: 28900
- Keywords: github, repository, basically, called, tackle, cluster, resource, status, contributor, source, repositories, plugin, essentially, actually, configuration, testing, created, request

### Resumo baseado na transcript

hello everyone thanks for stopping by our session and we hope you've been having an amazing conference so far our talk today is going to be about on a topic which is close to every contributor but it is a nightmare for every implementer at least that is what we feel like just a couple of days ago in the contributor summit we actually met someone who was trying to implement prow which we'll cover don't worry that's what we're here for and they faced a lot of trouble and

### Excerpt da transcript

hello everyone thanks for stopping by our session and we hope you've been having an amazing conference so far our talk today is going to be about on a topic which is close to every contributor but it is a nightmare for every implementer at least that is what we feel like just a couple of days ago in the contributor summit we actually met someone who was trying to implement prow which we'll cover don't worry that's what we're here for and they faced a lot of trouble and that sort of just reinforced our own belief that prow is something every contributor everyone who has made a pulled request to kubernetes is at least somewhat familiar with they have seen it comment on their pr or their issue but they've liked it but when it comes to installing it for their own repos or setting it up or just understanding what is happening behind the scenes of prow how it is working that is not clear and that is what we aim to solve in this talk we aim that once you go through our session after this you feel confident enough in trying out prow on your own installing it on your repositories and basically having fun with it so before we begin a bit of introductions are in order who are we i am sharma i work as a developer and experience engineer at octato i also actively contribute to the kubernetes project i will be leading the ci signal team in the 125 release and i'm a new contributor ambassador for kubernetes sig docs where i help people contribute to the project i'll hand over to nabarron now hey everyone i'm nabarun i work as a senior engineer at vmware i have been contributing to kubernetes for the past three years and spent around two and a half years contributing to sig release having led kubernetes 1.21 last year which is going to be deprecated this month next week possibly and i'm also the current currently a release manager uh in the communities release engineering uh sub project i am also an elected member of the kubernetes code of conduct committee um i have been uh in the committee for the past eight or so months besides that i helped maintaining some other areas in communities like github administration and contributing to other areas of the project now why are we here what is prop is a kubernetes based cicd system being based on top of kubernetes it brings all the pros of running any application of kubernetes like you get replication you get scaling you get rolling updates you get highly available nature of any stateless workload that you usually run on kubern
