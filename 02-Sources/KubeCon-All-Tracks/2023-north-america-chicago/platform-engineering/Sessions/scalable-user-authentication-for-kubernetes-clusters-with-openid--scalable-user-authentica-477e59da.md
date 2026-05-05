---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Platform Engineering"
themes: ["Security", "Platform Engineering", "Kubernetes Core", "SRE Reliability"]
speakers: ["Nathan Brahms", "Shashwat Sehgal", "P0 Security"]
sched_url: https://kccncna2023.sched.com/event/1R2o1/scalable-user-authentication-for-kubernetes-clusters-with-openid-connector-nathan-brahms-shashwat-sehgal-p0-security
youtube_search_url: https://www.youtube.com/results?search_query=Scalable+User+Authentication+for+Kubernetes+Clusters+with+OpenID+Connector+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Scalable User Authentication for Kubernetes Clusters with OpenID Connector - Nathan Brahms & Shashwat Sehgal, P0 Security

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Security]], [[Platform Engineering]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Nathan Brahms, Shashwat Sehgal, P0 Security
- Schedule: https://kccncna2023.sched.com/event/1R2o1/scalable-user-authentication-for-kubernetes-clusters-with-openid-connector-nathan-brahms-shashwat-sehgal-p0-security
- Busca YouTube: https://www.youtube.com/results?search_query=Scalable+User+Authentication+for+Kubernetes+Clusters+with+OpenID+Connector+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Scalable User Authentication for Kubernetes Clusters with OpenID Connector.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2o1/scalable-user-authentication-for-kubernetes-clusters-with-openid-connector-nathan-brahms-shashwat-sehgal-p0-security
- YouTube search: https://www.youtube.com/results?search_query=Scalable+User+Authentication+for+Kubernetes+Clusters+with+OpenID+Connector+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YqW-R-4HRgE
- YouTube title: Scalable User Authentication for Kubernetes Clusters with OpenID... Nathan Brahms & Shashwat Sehgal
- Match score: 0.89
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/scalable-user-authentication-for-kubernetes-clusters-with-openid-conne/YqW-R-4HRgE.txt
- Transcript chars: 21236
- Keywords: authentication, access, terraform, authorization, cluster, delete, security, application, request, identity, provider, configure, source, environment, probably, credential, actually, already

### Resumo baseado na transcript

my name is Nathan brahs I'm one of the co-founders of a company called pzer security I'm joined today by my co-founder shashwat another founder of pz security and today we're going to talk to you about how you can help add scalable user authentication to your kubernetes clusters using a technology called open ID connect so in today's talk I'm first going to give a little primer on how access in kubernetes works I'm going to break down access in its two constituent Parts authentication and authorization most of

### Excerpt da transcript

my name is Nathan brahs I'm one of the co-founders of a company called pzer security I'm joined today by my co-founder shashwat another founder of pz security and today we're going to talk to you about how you can help add scalable user authentication to your kubernetes clusters using a technology called open ID connect so in today's talk I'm first going to give a little primer on how access in kubernetes works I'm going to break down access in its two constituent Parts authentication and authorization most of today's talk is going to be consumed with authentication I'm going to talk about what you might want to consider when you're adding authentication to a kubernetes cluster and what the trade-offs are that you have to think about it's probably not a big surprise but one of the options I'm going to Advocate that you highly consider is open ID connect or oidc I'll then talk about what's involved in adding oid C to a kubernetes cluster as part of this talk we're going to give you access to a public open source repo with some terraform templates that you can use to set up oidc in your own kubernetes cluster and I'll give you a demo of setting up oidc in a live cluster using those terraform templates and then finally at the very end we're going to have a few minutes where we can talk about how you might think about scalability for authorization cool so let's get started so let's talk about access in kubernetes and we're going to start with this simple command you might want to run in a kubernetes cluster delete a pod right you're going to use Cube cuddle the client uh Library what does Cube cuddle delete pod do well Cube cuddle delete pod is really just a thin wrapper around a web request that's sent to the kubernetes API server this web request looks like this it says delete blah blah blah pods blah blah blah and then it has an authorization header that contains some sort of credential and that credential is going to author uh present who is making the request so what does kubernetes do with this web request so kubernetes has to decide whether or not you can execute this web request and in a very oversimplified pseudo code it does something like this first it takes that authorization credential that you passed in that header and tries to figure out who you are that's authentication kubernetes doesn't have one way it can do authentication it has several and you as a kubernetes maintainer can choose which of those methods you want to use after it's figured o
