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
speakers: ["Shubham Chaudhary", "Sayan Mondal", "Harness"]
sched_url: https://kccnceu2024.sched.com/event/1YhiW/fire-in-the-cloud-bringing-managed-services-under-the-ambit-of-cloud-native-chaos-engineering-shubham-chaudhary-sayan-mondal-harness
youtube_search_url: https://www.youtube.com/results?search_query=Fire+in+the+Cloud%3A+Bringing+Managed+Services+Under+the+Ambit+of+Cloud-Native+Chaos+Engineering+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Fire in the Cloud: Bringing Managed Services Under the Ambit of Cloud-Native Chaos Engineering - Shubham Chaudhary & Sayan Mondal, Harness

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Shubham Chaudhary, Sayan Mondal, Harness
- Schedule: https://kccnceu2024.sched.com/event/1YhiW/fire-in-the-cloud-bringing-managed-services-under-the-ambit-of-cloud-native-chaos-engineering-shubham-chaudhary-sayan-mondal-harness
- Busca YouTube: https://www.youtube.com/results?search_query=Fire+in+the+Cloud%3A+Bringing+Managed+Services+Under+the+Ambit+of+Cloud-Native+Chaos+Engineering+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Fire in the Cloud: Bringing Managed Services Under the Ambit of Cloud-Native Chaos Engineering.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YhiW/fire-in-the-cloud-bringing-managed-services-under-the-ambit-of-cloud-native-chaos-engineering-shubham-chaudhary-sayan-mondal-harness
- YouTube search: https://www.youtube.com/results?search_query=Fire+in+the+Cloud%3A+Bringing+Managed+Services+Under+the+Ambit+of+Cloud-Native+Chaos+Engineering+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=xCDQp5E3VUs
- YouTube title: Fire in the Cloud: Bringing Managed Services Under the Ambit of Cloud-Native Chaos Engineering
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/fire-in-the-cloud-bringing-managed-services-under-the-ambit-of-cloud-n/xCDQp5E3VUs.txt
- Transcript chars: 29599
- Keywords: experiment, specific, engineering, generate, support, manage, litmus, multiple, experiments, actual, provide, running, specifically, litmas, everything, create, lambda, control

### Resumo baseado na transcript

hey guys hope you guys are enjoying coupon uh thanks for joining in in this maintainer track so we'll be talking about uh litmus chos uh we are the maintenance of Li sces we'll see about a spage soon but this is our talk uh bringing fire in the cloud which is uh talking about manage services because most of us use manage services to manage our community's workloads so we'll be specifically looking into what causes problems in manage services and how we can mitigate them using lmus and

### Excerpt da transcript

hey guys hope you guys are enjoying coupon uh thanks for joining in in this maintainer track so we'll be talking about uh litmus chos uh we are the maintenance of Li sces we'll see about a spage soon but this is our talk uh bringing fire in the cloud which is uh talking about manage services because most of us use manage services to manage our community's workloads so we'll be specifically looking into what causes problems in manage services and how we can mitigate them using lmus and we'll also talk about litmas so those of you who are litmas users or new to litmas uh should uh you know get a good experience around it and then probably hopefully start contributing and be a part of the community so this is us I am cheyen and he is sham I'm a senior soft engineer at harness and also a maintainer of itmas and Sham if you like uh I'm I'm also senior software engineer at harness and M at litmas cool so we both will be sharing some lmus wisdom hopefully and let me start by jumping into the dependency dilemma that we face today so a lot of us use manage services a lot of us are reliant on manage services because not everybody has everything on Prem like their own Data Center and everything it's costly so a lot of people use manage services now the problems that we get is a lack of control obviously because we have limited visibility on what they are providing us so we base our service is based on something that's theirs so that is one thing lack of control which we don't like second is the vendor lock in uh you might argue that we don't really have vendor lockin since we have uh our systems set up in multiple Cloud so that way we can pull everything out from one shift it to the other but there's definitely a vendor lock in because the layer between your services and the actual vendor providing it is opaque to you guys so there is a the vendor login uh because there are propriety technologies that they are using which might not be open to you in the vacuum and then there's a trust issue obviously so the availability reliability uh up type everything is based on what they promise you but yeah it's a trust Factor cool so before jumping into chos engineering this is a scarce SL because outages are expensive and these are some experiments I'm not calling anybody out trust me but yeah these are some of the actual outages that had happened and this causes uh sort of a you know a fear or what do we say we don't really like having outages because of things like this uh i
