---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Security"
themes: ["Security", "Kubernetes Core"]
speakers: ["Yuan Chen", "James Munnelly", "Apple Inc."]
sched_url: https://kccncna2023.sched.com/event/1R2p3/securing-kubernetes-migrating-from-long-lived-to-time-bound-tokens-without-disrupting-existing-apps-yuan-chen-james-munnelly-apple-inc
youtube_search_url: https://www.youtube.com/results?search_query=Securing+Kubernetes%3A+Migrating+from+Long-Lived+to+Time-Bound+Tokens+Without+Disrupting+Existing+Apps+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Securing Kubernetes: Migrating from Long-Lived to Time-Bound Tokens Without Disrupting Existing Apps - Yuan Chen & James Munnelly, Apple Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Chicago
- Speakers: Yuan Chen, James Munnelly, Apple Inc.
- Schedule: https://kccncna2023.sched.com/event/1R2p3/securing-kubernetes-migrating-from-long-lived-to-time-bound-tokens-without-disrupting-existing-apps-yuan-chen-james-munnelly-apple-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Securing+Kubernetes%3A+Migrating+from+Long-Lived+to+Time-Bound+Tokens+Without+Disrupting+Existing+Apps+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Securing Kubernetes: Migrating from Long-Lived to Time-Bound Tokens Without Disrupting Existing Apps.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2p3/securing-kubernetes-migrating-from-long-lived-to-time-bound-tokens-without-disrupting-existing-apps-yuan-chen-james-munnelly-apple-inc
- YouTube search: https://www.youtube.com/results?search_query=Securing+Kubernetes%3A+Migrating+from+Long-Lived+to+Time-Bound+Tokens+Without+Disrupting+Existing+Apps+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=URGPfegNz64
- YouTube title: Securing Kubernetes: Migrating from Long-Lived to Time-Bound Tokens Wi... Yuan Chen & James Munnelly
- Match score: 0.836
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/securing-kubernetes-migrating-from-long-lived-to-time-bound-tokens-wit/URGPfegNz64.txt
- Transcript chars: 29905
- Keywords: tokens, account, actually, secret, automatically, feature, tracking, request, working, create, expiration, running, secure, generate, secrets, expired, extend, important

### Resumo baseado na transcript

okay let's get started welcome to the session I hope everyone has enjoyed their Day At cubec Con I'm yanen from Apple cloud services team I've been working on Apple kubernetes infrastructure I've been a active contributor to CES project with a focus on SC security is something new to me so I'm still learning um and yeah I'm also at Apple over in the field engineering team so helping work with various customers across uh across the company to make sure that they're kind of successful on our kubernetes

### Excerpt da transcript

okay let's get started welcome to the session I hope everyone has enjoyed their Day At cubec Con I'm yanen from Apple cloud services team I've been working on Apple kubernetes infrastructure I've been a active contributor to CES project with a focus on SC security is something new to me so I'm still learning um and yeah I'm also at Apple over in the field engineering team so helping work with various customers across uh across the company to make sure that they're kind of successful on our kubernetes platforms and working with you on this migration okay here is the agenda of our talk I'm going to give a introduction overview of different service account token kubernetes and parameters and feature gate BS that can be used to manage to configure the tokens in kubernetes then all different kind of the tokens their implications and potential impact on different use cases I will also talk about and how to track and monitor the different service account tokens in kues then JS will Deep dive into how can we and simy and upgrade or transition from the traditional old neacy token to the more Dynamic time Bond and more secure tokens so if we look at the service and account token API token Ines uh token is a pieces of information that authenticate application container port to API servers it's very important to secure and manage tokens properly because token and uh this is used to Grant class resources to different applications any of the compromise right can have significant uh security implications so traditionally as you may know right and uh the nexy token is based on the use the secret so when you create a service account it automatically and generate uh secrets with the tokens this token never and expired so it's there secure also the service accounts can be shared by multiple or different applications so that's also make it n secure so it's definitely it's not recommended but unfortunately in a lot of the Clusters neacy application and workload may still use the uh old tokens and neacy and non leave the secret secret based tokens so now of course we are and moving to this and more Dynamic and time limited tokens and acquire aend and by from the token the request API then application or the kubernets will refresh renot it automatically or periodically and one example is spond and service token for the ports finally there are still in the sum and the long leave the token if you really need it you can manually create a secret and associate with the uh service acc
