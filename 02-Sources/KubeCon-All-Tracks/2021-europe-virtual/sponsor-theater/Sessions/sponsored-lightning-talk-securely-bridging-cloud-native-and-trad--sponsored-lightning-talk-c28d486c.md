---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Sponsor Theater"
themes: ["Security"]
speakers: ["Daniel Feldman", "HPE"]
sched_url: https://kccnceu2021.sched.com/event/igUc/sponsored-lightning-talk-securely-bridging-cloud-native-and-traditional-workloads-with-spire-daniel-feldman-hpe
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Lightning+Talk%3A+Securely+Bridging+Cloud-Native+and+Traditional+Workloads+with+SPIRE+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Sponsored Lightning Talk: Securely Bridging Cloud-Native and Traditional Workloads with SPIRE - Daniel Feldman, HPE

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Sponsor Theater]]
- Temas: [[Security]]
- País/cidade: Virtual / Virtual
- Speakers: Daniel Feldman, HPE
- Schedule: https://kccnceu2021.sched.com/event/igUc/sponsored-lightning-talk-securely-bridging-cloud-native-and-traditional-workloads-with-spire-daniel-feldman-hpe
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Lightning+Talk%3A+Securely+Bridging+Cloud-Native+and+Traditional+Workloads+with+SPIRE+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Sponsored Lightning Talk: Securely Bridging Cloud-Native and Traditional Workloads with SPIRE.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/igUc/sponsored-lightning-talk-securely-bridging-cloud-native-and-traditional-workloads-with-spire-daniel-feldman-hpe
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Lightning+Talk%3A+Securely+Bridging+Cloud-Native+and+Traditional+Workloads+with+SPIRE+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=gNSdHCAbAgI
- YouTube title: Sponsored Lightning Talk: Securely Bridging Cloud-Native and Traditional Workloads... Daniel Feldman
- Match score: 0.984
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/sponsored-lightning-talk-securely-bridging-cloud-native-and-traditiona/gNSdHCAbAgI.txt
- Transcript chars: 3859
- Keywords: identity, talking, spiffy, server, secure, workload, lightning, organization, traditional, identities, connections, aspire, securely, bridging, workloads, thanks, resources, clouds

### Resumo baseado na transcript

hello everyone welcome to kubecon eu 2021 and thanks for joining my lightning talk my name is daniel feldman and i'm a software engineer at hewlett packard enterprise and today we'll be talking about securely bridging cloud native and traditional workloads with spire in a traditional organization we implemented security through strong perimeters we have network level devices like firewalls and vpns that connect your users to the right resources but as we add new services new data centers new clouds new regions within one cloud then this becomes too

### Excerpt da transcript

hello everyone welcome to kubecon eu 2021 and thanks for joining my lightning talk my name is daniel feldman and i'm a software engineer at hewlett packard enterprise and today we'll be talking about securely bridging cloud native and traditional workloads with spire in a traditional organization we implemented security through strong perimeters we have network level devices like firewalls and vpns that connect your users to the right resources but as we add new services new data centers new clouds new regions within one cloud then this becomes too hard to manage and secure spire is the solution to this problem with spire a single identity provider distributes secure identities to all the services within your organization and then once each service has its own identity they can establish secure connections now when i refer to identity i mean two concrete things either a x 509 certificate or a job and they both have two different uses for establishing different kinds of secure connections between your resources now you've already heard me use the term spiffy inspire spiffy is the standard for implementing the service identity layer and then spire is a specific implementation of the spiffy standard they're both cncf projects they're open source there are many companies involved and you can join any of our meetings and contribute to any one of them on the left we've got a little bit of a timeline of the spiffy inspire history this technology goes all the way back to the early 2000s at bell labs where they were developing service identity technology then google developed something similar netflix developed something similar kubernetes came out in 2015 and immediately had the need for some kind of a service identity layer so this goes way back in 2017 spiffy and spire were introduced and then in 2018 very early on a couple big hyperscalers including uber tick tock and square adopted aspire as their service identity layer now in 2021 we're seeing growing adoption of both of these technologies so let's go through a quick summary of how spire works first of all there are two components there's aspire server and aspire agent now when the agent starts up its first job is to prove its identity to the server so it provides some bit of information that allows the spire server to verify its identity and then the spire server can go out to cloud apis like aws azure google cloud can go out to the kubernetes api and verify the identity of the spire agent then once the spir
