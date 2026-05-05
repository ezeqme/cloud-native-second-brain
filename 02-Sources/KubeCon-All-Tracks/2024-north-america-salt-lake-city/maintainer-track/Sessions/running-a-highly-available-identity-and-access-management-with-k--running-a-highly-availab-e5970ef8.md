---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Ryan Emerson", "Kameswararao Akella", "Red Hat"]
sched_url: https://kccncna2024.sched.com/event/1hoyn/running-a-highly-available-identity-and-access-management-with-keycloak-ryan-emerson-kameswararao-akella-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Running+a+Highly+Available+Identity+and+Access+Management+with+Keycloak+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Running a Highly Available Identity and Access Management with Keycloak - Ryan Emerson & Kameswararao Akella, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Ryan Emerson, Kameswararao Akella, Red Hat
- Schedule: https://kccncna2024.sched.com/event/1hoyn/running-a-highly-available-identity-and-access-management-with-keycloak-ryan-emerson-kameswararao-akella-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Running+a+Highly+Available+Identity+and+Access+Management+with+Keycloak+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Running a Highly Available Identity and Access Management with Keycloak.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hoyn/running-a-highly-available-identity-and-access-management-with-keycloak-ryan-emerson-kameswararao-akella-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Running+a+Highly+Available+Identity+and+Access+Management+with+Keycloak+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=gDFWBQO31M4
- YouTube title: Running a Highly Available Identity and Access Management with Keycloak - R. Emerson, K. Akella
- Match score: 0.962
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/running-a-highly-available-identity-and-access-management-with-keycloa/gDFWBQO31M4.txt
- Transcript chars: 28410
- Keywords: keycloak, availability, infinispan, database, server, requests, instance, available, cluster, accelerator, aurora, architecture, provide, network, already, single, within, balancer

### Resumo baseado na transcript

my name is Kish and he is Ryan we are um software Engineers from Red um and we are going to talk about highly available keycloak and how we go about it how you uh how many of you already use keycloak um show off hands awesome for how uh how many of you are attending Cube on for the first time pretty much it overlaps very well and thank you for sticking around till the end of cubec con to attend this and hopefully it will be a good

### Excerpt da transcript

my name is Kish and he is Ryan we are um software Engineers from Red um and we are going to talk about highly available keycloak and how we go about it how you uh how many of you already use keycloak um show off hands awesome for how uh how many of you are attending Cube on for the first time pretty much it overlaps very well and thank you for sticking around till the end of cubec con to attend this and hopefully it will be a good takeaway uh for you all um so all right I think most of us saw this slide in the keynote today and Cube um keycloak uh is a incubating part project and we are in that uh Chasm phase and we always uh intend to explore the opportunities to improve kylo and making it highly available is one of the aspects of it um little bit of what we want to do today is to introduce keycloak and explain what it means um for organizations and users alike uh initially and we'll go more uh into the details of how we achieve High availability and on all right what is the identity and access management and do you need one um most of us if we put some credentials inside uh an application yes we would need one um to keep our uh content secure and provide easier access to the users and provide more seamless experience uh using single sign on and how does that work um a user logs in to keycloak and he requests for a token to access a particular resource keycloak makes sure the user is um allowed to do that and verifies the token and provides the access and there are multiple ways to do it using OD z o n and different things that you do on an identity and access management platform is to manage users uh manage their credentials permissions handle user registration uh password uh reset and handling and integrating the IM IM platform into your existing security infrastructure so single sign on is cool on day one you your users now only have to remember one password and only authenticate maybe once a day depending upon your session TTL and you could also make it more secure using um additional authentication like multiactor authentication pass Keys Etc you can customize now your front end of the login um using custom themes make sense already for like a small application right and this is how it will look uh when you first open key cloak once it's configured the login screen for your applications and but this is all good for day one how about day two now we look at integrating our existing security infrastructure with keylo like alap and caros we would want to
