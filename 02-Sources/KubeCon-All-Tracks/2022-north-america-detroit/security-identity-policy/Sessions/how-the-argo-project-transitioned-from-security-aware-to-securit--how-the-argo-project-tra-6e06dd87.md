---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Security + Identity + Policy"
themes: ["Security", "GitOps Delivery"]
speakers: ["Henrik Blixt", "Michael Crenshaw", "Intuit"]
sched_url: https://kccncna2022.sched.com/event/182Gc/how-the-argo-project-transitioned-from-security-aware-to-security-first-henrik-blixt-michael-crenshaw-intuit
youtube_search_url: https://www.youtube.com/results?search_query=How+the+Argo+Project+Transitioned+From+Security+Aware+To+Security+First+CNCF+KubeCon+2022
slides: []
status: parsed
---

# How the Argo Project Transitioned From Security Aware To Security First - Henrik Blixt & Michael Crenshaw, Intuit

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]], [[GitOps Delivery]]
- País/cidade: United States / Detroit
- Speakers: Henrik Blixt, Michael Crenshaw, Intuit
- Schedule: https://kccncna2022.sched.com/event/182Gc/how-the-argo-project-transitioned-from-security-aware-to-security-first-henrik-blixt-michael-crenshaw-intuit
- Busca YouTube: https://www.youtube.com/results?search_query=How+the+Argo+Project+Transitioned+From+Security+Aware+To+Security+First+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre How the Argo Project Transitioned From Security Aware To Security First.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Gc/how-the-argo-project-transitioned-from-security-aware-to-security-first-henrik-blixt-michael-crenshaw-intuit
- YouTube search: https://www.youtube.com/results?search_query=How+the+Argo+Project+Transitioned+From+Security+Aware+To+Security+First+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=EilOEF4gs0c
- YouTube title: How the Argo Project Transitioned From Security Aware To Security First - Henrik & Michael Crenshaw
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/how-the-argo-project-transitioned-from-security-aware-to-security-firs/EilOEF4gs0c.txt
- Transcript chars: 31518
- Keywords: security, argo, projects, source, process, actually, started, vendor, product, talked, maintainers, interest, channel, release, vulnerability, vendors, embargo, patches

### Resumo baseado na transcript

so I'm Michael Crenshaw I'm a software engineer at Intuit on the Argo CD team my name is Henry Flix I'm a product manager also at Intuit and one of the Argo maintainers no mouse there we go so just uh quickly since we're both from into just want to give you a quick introduction to who we are and give you a little bit understanding where we're coming from so uh we're a financial technology software company based in the US we have most of our business in the

### Excerpt da transcript

so I'm Michael Crenshaw I'm a software engineer at Intuit on the Argo CD team my name is Henry Flix I'm a product manager also at Intuit and one of the Argo maintainers no mouse there we go so just uh quickly since we're both from into just want to give you a quick introduction to who we are and give you a little bit understanding where we're coming from so uh we're a financial technology software company based in the US we have most of our business in the US and we spent the last few years building a platform uh that comprised of Five Pillars to modernize our our infrastructure so we now have moved all all our services to this platform and this platform now serves about 58 billion machine learning predictions per day and during tax peak season which is our main time of year we push about 3.6 billion requests through this platform uh if you look at the dev environment that we have when when our teams go in and create a new application to build to build a service we we automatically uh bend a namespace and a bunch of other things automatically for them for that application so we have about 16 000 name spaces uh in in our environment for the 3000 ish services that we have running and these are developed by the 6000 plus developers that that we have that work on on all the services for those those those products that that we have so this platform and this journey that we've been on for the last few years has has given us a six-fold increase in developer uh productivity so that's a huge lift and a huge benefit to all our developers and Argo has been one of the key parts parts of that we're also strong Believers in in open source as some of you probably know uh Argo the Argo project came from into it originally and but we also have other projects we're also have involved in the community in other areas like kubernetes istio we have a new project called Neymar project we announced here very recently and we try and and contribute and work with the open source communities communities as much as we can and this was also recognized in 2019 when we won the end use reward and for those of you that were in the keynote on Wednesday we actually wanted again um this the this year so big thank you to the end user Community for for the recognition we're really happy and proud over that but this talked about Argo not into it so just a little quick background for those who they don't know Argo which I'm guessing is not too many of you but uh one thing you probably don't know
