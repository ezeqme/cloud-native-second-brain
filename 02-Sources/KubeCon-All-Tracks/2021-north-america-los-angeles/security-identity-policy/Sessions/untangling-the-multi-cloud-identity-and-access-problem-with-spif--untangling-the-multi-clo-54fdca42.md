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
themes: ["Security"]
speakers: ["Brandon Lum", "Mariusz Sabath", "IBM"]
sched_url: https://kccncna2021.sched.com/event/lV3k/untangling-the-multi-cloud-identity-and-access-problem-with-spiffe-tornjak-brandon-lum-mariusz-sabath-ibm
youtube_search_url: https://www.youtube.com/results?search_query=Untangling+the+Multi-Cloud+Identity+and+Access+Problem+With+SPIFFE+Tornjak+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Untangling the Multi-Cloud Identity and Access Problem With SPIFFE Tornjak - Brandon Lum & Mariusz Sabath, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]]
- País/cidade: United States / Los Angeles
- Speakers: Brandon Lum, Mariusz Sabath, IBM
- Schedule: https://kccncna2021.sched.com/event/lV3k/untangling-the-multi-cloud-identity-and-access-problem-with-spiffe-tornjak-brandon-lum-mariusz-sabath-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=Untangling+the+Multi-Cloud+Identity+and+Access+Problem+With+SPIFFE+Tornjak+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Untangling the Multi-Cloud Identity and Access Problem With SPIFFE Tornjak.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV3k/untangling-the-multi-cloud-identity-and-access-problem-with-spiffe-tornjak-brandon-lum-mariusz-sabath-ibm
- YouTube search: https://www.youtube.com/results?search_query=Untangling+the+Multi-Cloud+Identity+and+Access+Problem+With+SPIFFE+Tornjak+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Voy_8wifB0E
- YouTube title: Untangling the Multi-Cloud Identity and Access Problem With SPIFFE Tornjak - B Lum & M Sabath
- Match score: 0.988
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/untangling-the-multi-cloud-identity-and-access-problem-with-spiffe-tor/Voy_8wifB0E.txt
- Transcript chars: 19410
- Keywords: identity, workload, access, identities, organization, provider, universal, workloads, cluster, clouds, federation, clusters, management, mission, create, manage, scheme, policy

### Resumo baseado na transcript

good to be here back in person um so today we're going to talk about a couple things we're going to be talking about um workflow identity we're going to be talking about multi-cloud and more specifically we're going to be talking about the multi-cloud access problem and how we are going to solve this with workload identity and technology such as spiffy spire and tanya so before we go ahead a little quick introduction my name is brandon and i'm here with my colleague marush and we are both

### Excerpt da transcript

good to be here back in person um so today we're going to talk about a couple things we're going to be talking about um workflow identity we're going to be talking about multi-cloud and more specifically we're going to be talking about the multi-cloud access problem and how we are going to solve this with workload identity and technology such as spiffy spire and tanya so before we go ahead a little quick introduction my name is brandon and i'm here with my colleague marush and we are both from ibm research and today we are going to start by telling you a bit more about workload identity uh how it works in a cloud provider we're then going to bring this into multi-cloud context and we're going to talk about solutions that work today and some of their limitations and then we are going to introduce this notion of a universal or organization-wide identity of which we have a really cool demo for you so we have a lot of content to dive into so let's go ahead um so let's first introduce the concept of vocal identity by looking at uh the ana the anatomy of a vocal identity within a context of a single cloud so every cloud provider kind of handles uh local identity in a similar way so each of them have has an identity provider that comes in the form of a root of trust or certificate authority this certificate authority then issues identities um through the form of usually some kind of infrastructure service such as you know for aws example would be the aws metadata service so we then have a workload that's running on let's say kubernetes or openshift uh this container that wants to access a service such as a database uh what they have to do is then they have to talk to the service to obtain a workload identity that comes in the form of usually a x 509 certificate or jw key token they then present this to the identity and access management on the top of the cloud and because you know the cloud is well integrated with itself it's able to authenticate the workbook identity and provide access seamlessly so now let's talk about this in terms of multi-cloud in this scenario we have an organization example where we have three different clouds we have ibm cloud we have s0 and aws and blue green and yellow respectively so we notice that if a workload kind of lives within its own silo we don't really have that much of a problem and in fact within a single cloud im identity access management is pretty much a solved problem however the difficulty comes in when we all do multi-
