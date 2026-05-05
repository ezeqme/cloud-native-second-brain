---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Alice Frosi", "Jakob Naucke", "Red Hat"]
sched_url: https://kccnceu2026.sched.com/event/2CW5s/enforce-vip-access-only-through-node-attestation-alice-frosi-jakob-naucke-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Enforce+VIP+Access+Only+Through+Node+Attestation+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Enforce VIP Access Only Through Node Attestation - Alice Frosi & Jakob Naucke, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Alice Frosi, Jakob Naucke, Red Hat
- Schedule: https://kccnceu2026.sched.com/event/2CW5s/enforce-vip-access-only-through-node-attestation-alice-frosi-jakob-naucke-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Enforce+VIP+Access+Only+Through+Node+Attestation+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Enforce VIP Access Only Through Node Attestation.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW5s/enforce-vip-access-only-through-node-attestation-alice-frosi-jakob-naucke-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Enforce+VIP+Access+Only+Through+Node+Attestation+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3H3n-tZYmlY
- YouTube title: Enforce VIP Access Only Through Node Attestation - Alice Frosi & Jakob Naucke, Red Hat
- Match score: 0.824
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/enforce-vip-access-only-through-node-attestation/3H3n-tZYmlY.txt
- Transcript chars: 23699
- Keywords: confidential, machine, server, trustee, trusted, basically, values, station, cluster, reference, attestation, trusty, environment, secret, operator, important, signed, create

### Resumo baseado na transcript

We are both from Reddit and today we're going to talk about um uh not at the station and confidential computing. So uh let's imagine your cluster as an exclusive IP uh club uh where you have inside your more critical and important information and data and you want to uh guarantee that only allowed entity has access to it. Um and another detail I want to mention is that uh the operator and the components I uh presented are all uh written in Rust uh using uh using QRS for Kubernetes interaction. So here you can see already the definition of virtual machine and the important part is uh the launch security that enable SMP. Um so here you can see already that there is a create logs and if we monitor the uh trusty logs we will see at a certain point all the logs of the attestation. Uh if you are interested in the attestation uh policy and the uh resource policy, the demo also show them but I will skip for uh timing.

### Excerpt da transcript

Okay. So, hi everyone. Uh my name is Alicha Frosi and with me there is Jacob N. We are both from Reddit and today we're going to talk about um uh not at the station and confidential computing. So uh let's imagine your cluster as an exclusive IP uh club uh where you have inside your more critical and important information and data and you want to uh guarantee that only allowed entity has access to it. So outside there are all um malicious uh embed actor like malware malicious cloud administrator anymore in general entity that should not have allowed to access your data and try to sneak in. So as the bouncer control passes an ID uh our trusty is responsible to um guarantee that only allowed entity has access to your data. So during this presentation we are going to walk you through how we protect the system, how we uh um manage the guest list and the VIP list and uh node and machine can join the cluster and keeping at the same time the parties secure and not slowing down. So um why and how this is possible?

So this is possible thanks to confidential computing and here you have the definition from the confidential computing one sort. So there are exact there are two part of this definition that are important. So first of all confidential computing help us to um protect the data that are being used. So this was a a whole uh we were missing this in security. Traditionally we we we have well established technique to predict data trust the data in transi but we were missing the data that were compute used by uh the CPU during the computation. So this is the first part and benefit of confidential computing. The second is that it guarantee that your environment where your code is running is actually secure and confidential. So this of course opens uh the door of all the use cases that deals with regulated data and in more general uh data that are critical like uh health insurance data or in in general anything that uh um you want to keep secure. So uh in our presentation we are going to focus especially on confidential clusters.

Uh we call uh we call them trust execution cluster. So the boundary uh from what it's inside the confidential environment is the cluster itself and outside is the rest like for example the cloud providers. Um so this implied that each node in the cluster need to uh run on a confidential envir environment. So it needs to use either MDSVS or interdx or ARM. So we put our trust in the cluster administrator but not in the cloud provider. So u
