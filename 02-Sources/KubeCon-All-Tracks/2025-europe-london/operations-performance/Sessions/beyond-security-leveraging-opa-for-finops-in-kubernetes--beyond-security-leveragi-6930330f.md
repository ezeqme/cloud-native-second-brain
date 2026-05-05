---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Operations + Performance"
themes: ["Security", "Kubernetes Core", "SRE Reliability"]
speakers: ["Sathish Kumar Venkatesan", "DevOpsCloudJunction Foundation Inc."]
sched_url: https://kccnceu2025.sched.com/event/1tx9M/beyond-security-leveraging-opa-for-finops-in-kubernetes-sathish-kumar-venkatesan-devopscloudjunction-foundation-inc
youtube_search_url: https://www.youtube.com/results?search_query=Beyond+Security%3A+Leveraging+OPA+for+FinOps+in+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Beyond Security: Leveraging OPA for FinOps in Kubernetes - Sathish Kumar Venkatesan, DevOpsCloudJunction Foundation Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Security]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Sathish Kumar Venkatesan, DevOpsCloudJunction Foundation Inc.
- Schedule: https://kccnceu2025.sched.com/event/1tx9M/beyond-security-leveraging-opa-for-finops-in-kubernetes-sathish-kumar-venkatesan-devopscloudjunction-foundation-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Beyond+Security%3A+Leveraging+OPA+for+FinOps+in+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Beyond Security: Leveraging OPA for FinOps in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx9M/beyond-security-leveraging-opa-for-finops-in-kubernetes-sathish-kumar-venkatesan-devopscloudjunction-foundation-inc
- YouTube search: https://www.youtube.com/results?search_query=Beyond+Security%3A+Leveraging+OPA+for+FinOps+in+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=aiC7C56pE7I
- YouTube title: Beyond Security: Leveraging OPA for FinOps in Kubernetes - Sathish Kumar Venkatesan
- Match score: 0.895
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/beyond-security-leveraging-opa-for-finops-in-kubernetes/aiC7C56pE7I.txt
- Transcript chars: 20611
- Keywords: trying, policies, resources, policy, particular, cost, environment, workloads, request, create, basically, violations, whenever, namespace, gatekeeper, created, security, whatever

### Resumo baseado na transcript

Uh today we are going to talk about beyond security leveraging operetis. So today we will uh cover about uh the finaps challenges whatever we have in the kubernetes environments uh opa fundamentals uh and capabilities uh if you are not aware of opa and then like how we can extend opa to uh cost governance which So it's a problem like in the chargeback like if you are uh not able to charge it to the right team and then uh uh you like not able to like track keep track of like what's happening in your cloud environment. So this is a latest cast report which says like in a given in a group of uh Kubernetes clusters whatever they surveyed so it says like only 10%age of the CPU being utilized and then like only 30 23% of the memory being utilized So you can control the uh you can write policies for kubernetes terraformy and much more. Uh so I think like most of you are using OPA to like um security controls and then like make check for compliance and stuff.

### Excerpt da transcript

Hello everyone, good afternoon to thanks for coming for this talk. Uh today we are going to talk about beyond security leveraging operetis. My name is Satishh Kumar Wingen. I'm coming from Canada. Uh so I run a website uh DevOps cloud junction. So it's a community website. We talk about cloud native AI other technologies. Uh I'm passionate about computers, electronics, uh photography. I love to contribute to open source projects. Ive contributed multiple projects. I like to uh attend community events like cubecon. So today we will uh cover about uh the finaps challenges whatever we have in the kubernetes environments uh opa fundamentals uh and capabilities uh if you are not aware of opa and then like how we can extend opa to uh cost governance which is like fabs practices and then like I'll show some example phops policies which is written in rego and uh how we can adapt and then how we can implement in environment and towards the end maybe I will show a demo uh with set of policies uh I can which I have applied in my environment.

So just a quick overview of like what is PHOPS. So PHOPS is a practice um in a dynamic cloud environment. It's very hard for everyone to keep track of like what's happening in your cloud environment. So uh come up with this uh key goals uh in form. So make sure that the uh your cloud bills have visibility you can take you can view those uh cloud spin effectively and then optimize try to choose like what's the correct uh right size instance which you want to use and then go for like reservations uh instead of trying to use on demand to reduce cost and then operate basically like try to have a continuous process to identify and then remediate uh those uh uh overspend the PHOPS challenges whatever we have in the Kubernetes environment right now like in the flex era uh state report it says like 32%age of the resources underutilized uh and then there are like other common issues basically like overprovision resources there are like idle workloads uh and then nonoptimal node selection so whenever people try to provision those clusters we don't know like what's the right uh skew to choose so we just provision some skew and then like later we see like okay it's not uh effectively being used and then uh resource kota.

So like we don't specify we don't like restrict those uh workloads to have a required resources to be used instead of like we allow people to leverage whatever the underlying hardware uh it's capable of uh the resources an
