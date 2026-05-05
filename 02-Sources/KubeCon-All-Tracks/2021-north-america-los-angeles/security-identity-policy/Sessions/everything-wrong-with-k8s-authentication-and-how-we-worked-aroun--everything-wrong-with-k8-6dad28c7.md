---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Security + Identity + Policy"
themes: ["Security", "GitOps Delivery"]
speakers: ["Mo Khan", "Margo Crawford", "VMware"]
sched_url: https://kccncna2021.sched.com/event/lV5I/everything-wrong-with-k8s-authentication-and-how-we-worked-around-it-mo-khan-margo-crawford-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Everything+Wrong+with+K8s+Authentication+and+How+We+Worked+Around+It+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Everything Wrong with K8s Authentication and How We Worked Around It - Mo Khan & Margo Crawford, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]], [[GitOps Delivery]]
- País/cidade: United States / Los Angeles
- Speakers: Mo Khan, Margo Crawford, VMware
- Schedule: https://kccncna2021.sched.com/event/lV5I/everything-wrong-with-k8s-authentication-and-how-we-worked-around-it-mo-khan-margo-crawford-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Everything+Wrong+with+K8s+Authentication+and+How+We+Worked+Around+It+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Everything Wrong with K8s Authentication and How We Worked Around It.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV5I/everything-wrong-with-k8s-authentication-and-how-we-worked-around-it-mo-khan-margo-crawford-vmware
- YouTube search: https://www.youtube.com/results?search_query=Everything+Wrong+with+K8s+Authentication+and+How+We+Worked+Around+It+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=OCkTnElNE9M
- YouTube title: Everything Wrong with K8s Authentication and How We Worked Around It - Mo Khan & Margo Crawford
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/everything-wrong-with-k8s-authentication-and-how-we-worked-around-it/OCkTnElNE9M.txt
- Transcript chars: 28851
- Keywords: identity, cluster, impersonation, server, request, provider, impersonate, configuration, signing, authentication, certificates, around, pretty, trying, option, always, headers, infrastructure

### Resumo baseado na transcript

so hey everyone i am okan uh i work on identity solutions for vmware tanzu uh i have worked on kubernetes for over five years now and i have been co-chair for cigot for over three years and i'm margot crawford um i'm an engineer for vmware tanza as well working on pinniped which it simplifies the kubernetes auth experience after working on pinniped i've learned a lot more about the features and shortcomings of built-in kubernetes all so i'm excited to share some of those learnings cool so in

### Excerpt da transcript

so hey everyone i am okan uh i work on identity solutions for vmware tanzu uh i have worked on kubernetes for over five years now and i have been co-chair for cigot for over three years and i'm margot crawford um i'm an engineer for vmware tanza as well working on pinniped which it simplifies the kubernetes auth experience after working on pinniped i've learned a lot more about the features and shortcomings of built-in kubernetes all so i'm excited to share some of those learnings cool so in this talk we're going to talk about some of the capabilities of kubernetes auth today and some of the limitations then we'll look at some workarounds that we did to work around some of the limitations and then at the end we're going to try to look forward and see what we could do in the future to make things a little better so let's say you want to configure auth in your kubernetes environment right seems like a pretty simple straightforward ask so let's look at the cloud providers right because this is generally the entry point for most kubernetes users because the reality is managing your own kubernetes infrastructure is hard kubernetes does not handle that part of the problem right so if you're using gcp you're probably used to using the g cloud cli if you're using azure you're used to using their cli and if you're using eks you know you're used to their cli right so each of these platforms has their own integrated im solution right and this is totally fine if you're all in on a single platform right but what if you're not right what if you want to use a different identity provider right so traditional enterprises tend to have corporate active directory with their user identity right and it's likely that they want to continue to use that identity in their kubernetes clusters right you tend to have a pretty high investment in your identity infrastructure and it's pretty unreasonable to ask people to change that right and enterprises want the flexibility to use any cloud provider right after all kubernetes is meant to offer workload flexibility and mobility across the cloud platforms right but having a unified picture of your identity across the cloud providers is an important piece of that mobility so if you're trying to figure out how to authenticate with something other than built-in cloud provider auth you might find that kubernetes oidc ident authentication is a nice option openid connect or oidc is a pretty common protocol for authenticating with an external ide
