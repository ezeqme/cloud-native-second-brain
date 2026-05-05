---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Security"
themes: ["Security"]
speakers: ["Benjamin Dronen", "Ford Motor Company", "Anjali Telang", "Red Hat"]
sched_url: https://kccncna2024.sched.com/event/1i7s8/workload-identity-federation-stop-using-long-lived-credentials-benjamin-dronen-ford-motor-company-anjali-telang-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Workload+Identity+Federation+%E2%80%93+Stop+Using+Long-Lived+Credentials+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Workload Identity Federation – Stop Using Long-Lived Credentials - Benjamin Dronen, Ford Motor Company & Anjali Telang, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: United States / Salt Lake City
- Speakers: Benjamin Dronen, Ford Motor Company, Anjali Telang, Red Hat
- Schedule: https://kccncna2024.sched.com/event/1i7s8/workload-identity-federation-stop-using-long-lived-credentials-benjamin-dronen-ford-motor-company-anjali-telang-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Workload+Identity+Federation+%E2%80%93+Stop+Using+Long-Lived+Credentials+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Workload Identity Federation – Stop Using Long-Lived Credentials.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7s8/workload-identity-federation-stop-using-long-lived-credentials-benjamin-dronen-ford-motor-company-anjali-telang-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Workload+Identity+Federation+%E2%80%93+Stop+Using+Long-Lived+Credentials+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=qqayHSkiNXU
- YouTube title: Workload Identity Federation – Stop Using Long-Lived Credentials - Benjamin Dronen & Anjali Telang
- Match score: 0.885
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/workload-identity-federation-stop-using-long-lived-credentials/qqayHSkiNXU.txt
- Transcript chars: 29232
- Keywords: workload, identity, cluster, account, secret, tokens, issuer, application, federation, credentials, external, provider, providers, applications, actually, already, awesome, spiffy

### Resumo baseado na transcript

uh first off I'm Ben dronin I am a kubernetes platform engineer at Ford Motor Company I'm Angel dang I'm the principal product manager for open shift authentication and identity and uh we're going to be talking about workload identity Federation and why you should stop using longlived credentials so by a show of hands how many of you guys are using uh accessing Some Cloud resource from your kubernetes cluster okay how many of you are using workload identity Federation to do that okay so like a good number

### Excerpt da transcript

uh first off I'm Ben dronin I am a kubernetes platform engineer at Ford Motor Company I'm Angel dang I'm the principal product manager for open shift authentication and identity and uh we're going to be talking about workload identity Federation and why you should stop using longlived credentials so by a show of hands how many of you guys are using uh accessing Some Cloud resource from your kubernetes cluster okay how many of you are using workload identity Federation to do that okay so like a good number of you are already doing exactly what we're going to be talking about doing but wait how many of you are not doing that I mean you're using service account Keys client client secret okay so there's a lot of you so that's perfect we're glad you're here so for all those who raised their hands please stop doing that uh okay so um workload identity is required to uniquely identify a workload uh so that when it accesses the cluster and uh authenticates to other applications we are able to monitor it and track it right so good news is that kubernetes already comes with workload identity many of you raised your hands and uh you're aware of service accounts most of you are aware of service service accounts here right so um service accounts are treated just like any other user in kubernetes uh any other user or group you can apply arback policies to to the the service accounts and uh you can use them on the cluster for um uh communicating between services on the cluster you can also use them uh for for any external applications that want to run tasks and um automation on the cluster so thanks to the seot team for thinking through workload identity um you know very early on when they build uh kubernetes we are going to take a little bit of trip down memory l with how uh you know service accounts were and what was the landscape like pre uh kubernetes 1121 that's a long time back well actually not it's just three years back so um let's look at how it was I have to use the clicker yeah so this was the landscape just you know some 3 years back so you had uh service account tokens many of them had tokens that uh didn't expire and they were Long Live tokens you could use that to communicate between Services uh you could use that as I mentioned to run from external applications to run automated tasks on the cluster like creating an application running updating an application Etc um and then uh for services that wanted to talk to external entities well you couldn't use ser
