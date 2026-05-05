---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Karthik S", "Umasankar Mukkara", "Udit Gaurav", "ChaosNative", "Saiyam Pathak", "Civo"]
sched_url: https://kccnceu2022.sched.com/event/ytr7/cloud-native-chaos-engineering-with-litmuschaos-karthik-s-umasankar-mukkara-udit-gaurav-chaosnative-saiyam-pathak-civo
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Chaos+Engineering+with+LitmusChaos+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Cloud Native Chaos Engineering with LitmusChaos - Karthik S, Umasankar Mukkara & Udit Gaurav, ChaosNative; Saiyam Pathak, Civo

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: Karthik S, Umasankar Mukkara, Udit Gaurav, ChaosNative, Saiyam Pathak, Civo
- Schedule: https://kccnceu2022.sched.com/event/ytr7/cloud-native-chaos-engineering-with-litmuschaos-karthik-s-umasankar-mukkara-udit-gaurav-chaosnative-saiyam-pathak-civo
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Chaos+Engineering+with+LitmusChaos+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Cloud Native Chaos Engineering with LitmusChaos.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytr7/cloud-native-chaos-engineering-with-litmuschaos-karthik-s-umasankar-mukkara-udit-gaurav-chaosnative-saiyam-pathak-civo
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Chaos+Engineering+with+LitmusChaos+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=pMWqhS-F3tQ
- YouTube title: Cloud Native Chaos Engineering Preview With LitmusChaos
- Match score: 1.002
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/cloud-native-chaos-engineering-with-litmuschaos/pMWqhS-F3tQ.txt
- Transcript chars: 37963
- Keywords: litmus, engineering, workflow, experiments, experiment, center, control, create, cluster, workflows, native, reliability, observability, around, happening, platform, available, devops

### Resumo baseado na transcript

[Music] hello and welcome to this webinar about chaos engineering with litmus chaos i am um head of chaos engineering at harness along with me my colleague koptik is principal engineer at harness together we have created litmus chaos project around four years ago which is now a cncf incubating project here is a agenda we'll first look at why and what are chaos engineering and its relevance to cloud native and i'll also talk about uh how chaos generally matures in an organization that practices around devops then i'll

### Excerpt da transcript

[Music] hello and welcome to this webinar about chaos engineering with litmus chaos i am um head of chaos engineering at harness along with me my colleague koptik is principal engineer at harness together we have created litmus chaos project around four years ago which is now a cncf incubating project here is a agenda we'll first look at why and what are chaos engineering and its relevance to cloud native and i'll also talk about uh how chaos generally matures in an organization that practices around devops then i'll delve a little bit into um the introduction of nitmus it's features use cases there have been a lot of learnings about how litmus is used by community and enterprises i'll talk a little bit about the newly found use cases for litmus and at the end kartik will do a demo of how to get started with litmus and he'll show an example of running chaos uh using litmus and connecting new targets etc etc to the litmus based control plane so let's start with uh some facts around id that are happening today so we all know that digital services are growing fast and the digital traffic uh is growing at an alarming rate in the last few years and this is uh fueled by the digital transformation that's that's happening and one of the reasons why the digital transformation is happening at this rate is the enablement given by kubernetes and the transformation of id into digital uh world is actually fueled by the adoption of kubernetes because of this there is a change that's happening in devops as well there is a subsection of devops that we are calling as cloud native devops which is a little different than the traditional devops in that it's uh faster the deliveries happen in a more automated way the new set of tools that are happening the automation of uh applying the configuration upgrades overall delivery everything is happening fast service reliability is extremely important for businesses um so of course when you have less reliability it really means that you are facing service down times or outages which is not good the businesses can face financial and reputational damages so we all know the importance of service reliability for the businesses and in general all services are built for providing maximum reliability in that they are built the components or applications micro services are generally built with redundancy uh as a goal right and even with that we are seeing um outages uh happening right and this is because how much ever you build carefully the
