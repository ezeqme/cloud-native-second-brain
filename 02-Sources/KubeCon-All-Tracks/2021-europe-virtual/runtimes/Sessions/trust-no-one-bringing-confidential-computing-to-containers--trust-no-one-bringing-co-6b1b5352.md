---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Runtimes"
themes: ["AI ML", "Runtime Containers"]
speakers: ["Samuel Ortiz", "Intel", "Eric Ernst", "Apple"]
sched_url: https://kccnceu2021.sched.com/event/iE1z/trust-no-one-bringing-confidential-computing-to-containers-samuel-ortiz-intel-eric-ernst-apple
youtube_search_url: https://www.youtube.com/results?search_query=Trust+No+One%3A+Bringing+Confidential+Computing+to+Containers+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Trust No One: Bringing Confidential Computing to Containers - Samuel Ortiz, Intel & Eric Ernst, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Runtimes]]
- Temas: [[AI ML]], [[Runtime Containers]]
- País/cidade: Virtual / Virtual
- Speakers: Samuel Ortiz, Intel, Eric Ernst, Apple
- Schedule: https://kccnceu2021.sched.com/event/iE1z/trust-no-one-bringing-confidential-computing-to-containers-samuel-ortiz-intel-eric-ernst-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Trust+No+One%3A+Bringing+Confidential+Computing+to+Containers+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Trust No One: Bringing Confidential Computing to Containers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE1z/trust-no-one-bringing-confidential-computing-to-containers-samuel-ortiz-intel-eric-ernst-apple
- YouTube search: https://www.youtube.com/results?search_query=Trust+No+One%3A+Bringing+Confidential+Computing+to+Containers+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=zTn9Xt1k1OA
- YouTube title: Trust No One: Bringing Confidential Computing to Containers- Samuel Ortiz, Intel & Eric Ernst, Apple
- Match score: 0.843
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/trust-no-one-bringing-confidential-computing-to-containers/zTn9Xt1k1OA.txt
- Transcript chars: 24228
- Keywords: computing, confidential, container, running, software, runtime, containers, hardware, everything, inside, actually, technologies, protect, virtual, machine, create, workload, layers

### Resumo baseado na transcript

hi everyone i'm samuel ortiz from intel and together with eric ernst from apple we're going to talk about confidential computing and containers so confidential computing um this may sound like yet another cloud buzzword but we actually believe that the cloud computing technology is building and providing um a way to create a very interesting new threat model so if you look at the at the existing trust computing base for a typical guest running on the cloud it needs it includes sorry the all these layers here from

### Excerpt da transcript

hi everyone i'm samuel ortiz from intel and together with eric ernst from apple we're going to talk about confidential computing and containers so confidential computing um this may sound like yet another cloud buzzword but we actually believe that the cloud computing technology is building and providing um a way to create a very interesting new threat model so if you look at the at the existing trust computing base for a typical guest running on the cloud it needs it includes sorry the all these layers here from hardware to software including the hypervisor the the host operating system the host kernel the firmware everything must be trusted by the guest everything that's provided by the host must be trusted by the guest and what confidential computing and the related technologies is trying to build is a threat model where all the software layers provided by the host are actually no longer trusted so it's trying to remove each and every piece of software provided by the hosts out of the guest tcb this is very appealing um these essentially completely remove the host software stack from the guest ecb um including the host firmware the kernel the hypervisor everything is out and the interesting part of this is that the tenant is the only one that can see and modify its data no one else can see it no one else can can modify it and most importantly the infrastructure owner the csp the the the infrastructure provider does not need to be trusted anymore so this is a very interesting uh threat model how do we get there uh what needs to be provided by those computing uh computational computing technologies to build that threat model well the first thing is that the uh they need to protect the tenants data this is this is obvious i think uh if you don't want if you want to remove the whole software stack from from the guest tcb uh you want to make sure that the host software cannot see or tamper with the guest data and the tenants data but that's not enough we also need to let the tenant verify what it's running which software component is running how it's running and on top of which hardware is running and we're going to go through those requirements in a little bit of details so first we want computational computing technologies to protect our data and we kind of we can already do that our data can be in three different states it can be in transit that is typically where your data is is going through some networking pipes and we have tls we have vpns uh in when
