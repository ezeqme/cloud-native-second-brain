---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "SDLC"
themes: ["Security"]
speakers: ["Mario Loriedo", "Red Hat", "Satish Puranam", "Ford"]
sched_url: https://kccncna2023.sched.com/event/1R2v8/using-workload-identity-federation-to-increase-developers-productivity-at-ford-motor-company-mario-loriedo-red-hat-satish-puranam-ford
youtube_search_url: https://www.youtube.com/results?search_query=Using+Workload+Identity+Federation+to+Increase+Developers+Productivity+at+Ford+Motor+Company+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Using Workload Identity Federation to Increase Developers Productivity at Ford Motor Company - Mario Loriedo, Red Hat & Satish Puranam, Ford

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[SDLC]]
- Temas: [[Security]]
- País/cidade: United States / Chicago
- Speakers: Mario Loriedo, Red Hat, Satish Puranam, Ford
- Schedule: https://kccncna2023.sched.com/event/1R2v8/using-workload-identity-federation-to-increase-developers-productivity-at-ford-motor-company-mario-loriedo-red-hat-satish-puranam-ford
- Busca YouTube: https://www.youtube.com/results?search_query=Using+Workload+Identity+Federation+to+Increase+Developers+Productivity+at+Ford+Motor+Company+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Using Workload Identity Federation to Increase Developers Productivity at Ford Motor Company.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2v8/using-workload-identity-federation-to-increase-developers-productivity-at-ford-motor-company-mario-loriedo-red-hat-satish-puranam-ford
- YouTube search: https://www.youtube.com/results?search_query=Using+Workload+Identity+Federation+to+Increase+Developers+Productivity+at+Ford+Motor+Company+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=NYCFzNDdXTk
- YouTube title: Using Workload Identity Federation to Increase Developers Producti... Mario Loriedo & Satish Puranam
- Match score: 0.871
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/using-workload-identity-federation-to-increase-developers-productivity/NYCFzNDdXTk.txt
- Transcript chars: 26760
- Keywords: environment, development, account, identity, actually, workspace, started, around, container, operator, credentials, another, access, google, particular, cluster, environments, nothing

### Resumo baseado na transcript

hello everyone hello and uh this is almost the end of the day almost the end of uh of cucon so thanks to all of you to attending our talk um so we're all going to talk about uh workload identity Federation in particular for a particular use case that is um development environment on kubernetes and in the in particular in the Ford uh use case hello all welcome uh my name is Satish PanAm I am a technical leader and a cloud manager for various cloud services some

### Excerpt da transcript

hello everyone hello and uh this is almost the end of the day almost the end of uh of cucon so thanks to all of you to attending our talk um so we're all going to talk about uh workload identity Federation in particular for a particular use case that is um development environment on kubernetes and in the in particular in the Ford uh use case hello all welcome uh my name is Satish PanAm I am a technical leader and a cloud manager for various cloud services some of the things that I'm responsible and accountable for most of the things around kubernetes lot of cloud services in Azure and gcp uh Mario yes and my name is Mario I I work for redot uh as a software engineer I work on the developer tools organization uh in red hat and I've been working on Cloud development environment for the last seven years and we'll uh talk about that cool so just want to set the stage before we um hopefully try to cover all of these things um I want to just talk about few things like uh what are the challenges where we were facing along why we did this thing um what is a cloud development environment uh few things about kuties of like uh what is a service account service account token volume projection and how that can be used uh to do things like workload identity Federation or Federated identities so with that so I just do want to set some basic s know um context of how big we are what we are uh we started along about 2017 currently we do have like two ginormous bare metal mon monolithic bare metal clusters on Prem we have 50 plus uh uh kubernetes clusters running anywhere from Azure on Prem to gcp to plants spread over 2 and a 12,000 3,000 application teams around 8 and a half th000 name spaces last time we bothered to count that is some Journey right so we've been as I said earlier uh we've been in Journey since 2016 2017 we started doing kues and from there on we jumped down to things like open shift started with coros tectonic for those who are around to know about them then started the whole journey of leas privileges why because we were as the fleet size was growing people were running around with uh quite a bit of elevated privileges uh then we started working on how do you do as the fleet size increases how do you do configuration management of this Fleet then we started talking about as we entered into public clouds what is IAC looks like what do cicd look like uh then whole bunch of things kicked around around Cloud adoption primarily around gcp Azure and then we st
