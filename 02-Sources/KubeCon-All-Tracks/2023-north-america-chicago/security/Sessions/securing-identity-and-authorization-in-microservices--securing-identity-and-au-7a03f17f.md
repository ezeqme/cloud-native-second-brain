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
themes: ["Security"]
speakers: ["Atul Tulshibagwale", "SGNL"]
sched_url: https://kccncna2023.sched.com/event/1R2vc/securing-identity-and-authorization-in-microservices-atul-tulshibagwale-sgnl
youtube_search_url: https://www.youtube.com/results?search_query=Securing+Identity+and+Authorization+in+Microservices+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Securing Identity and Authorization in Microservices - Atul Tulshibagwale, SGNL

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: United States / Chicago
- Speakers: Atul Tulshibagwale, SGNL
- Schedule: https://kccncna2023.sched.com/event/1R2vc/securing-identity-and-authorization-in-microservices-atul-tulshibagwale-sgnl
- Busca YouTube: https://www.youtube.com/results?search_query=Securing+Identity+and+Authorization+in+Microservices+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Securing Identity and Authorization in Microservices.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2vc/securing-identity-and-authorization-in-microservices-atul-tulshibagwale-sgnl
- YouTube search: https://www.youtube.com/results?search_query=Securing+Identity+and+Authorization+in+Microservices+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=k4tusY8-pXs
- YouTube title: Securing Identity and Authorization in Microservices - Atul Tulshibagwale, SGNL
- Match score: 0.892
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/securing-identity-and-authorization-in-microservices/k4tusY8-pXs.txt
- Transcript chars: 33651
- Keywords: transaction, external, tokens, server, calling, trying, called, context, microservice, security, cannot, subject, shares, basically, information, request, result, compromise

### Resumo baseado na transcript

hi everyone uh thanks for uh spending time with me this afternoon and my apologies for having you squeeze into this tiny room but if I may ask uh if you can come even closer you'll be able to see this the code Snippets that I'm going to show later so if you want to do that you can move forward um so let me uh start by talking about myself uh I atag I'm the CTO of signal.

### Excerpt da transcript

hi everyone uh thanks for uh spending time with me this afternoon and my apologies for having you squeeze into this tiny room but if I may ask uh if you can come even closer you'll be able to see this the code Snippets that I'm going to show later so if you want to do that you can move forward um so let me uh start by talking about myself uh I atag I'm the CTO of signal. a sgnl and we're into continuous authorization or continuous access management and if you would like to know what that is uh you can all go to our website after my talk um and some of you might know me from my work on standards called The Continuous access evaluation protocol something I started when I was at Google and has now grown into this uh pretty um sort of big movement but this uh this presentation is about another exciting standard that I'm working on in the ietf called transaction tokens and it helps you uh secure your identity and authorization in microservices so let's get started so um why do we need this right so uh as you know like um any uh modern architecture you know external calls to an uh API or an application will result in a lot of calls internally to various microservices right and um the in this diagram that external API microservice encapsulates any like Network infrastructure that you might have right so um but the important thing is that these calls are shortlived right they they don't exceed a few minutes of execution at any given point of time and even if you have sort of map reduce or some large processes running they will finally result into calls that last a few uh minutes or less uh individually right so you can think of these internal calls that propagate through your uh internal Services as always being shortlived now um unfortunately there are a lot of attacks that are possible where a VPC might be compromised and as you might know some of the recent uh pretty um damaging attacks have been as a result of compromise of privileged users um that you know that were uh compromising the vpcs of companies right and this can result in user impersonation or you know arbitrary code and execution right and so extremely damaging uh to any Enterprise that needs so obviously we need to do more about security than what we have so today most commonly people use implicit trust if you're in the VPC you can just call any service and um you know it doesn't matter um because you're in the VPC you're fine you're trusted which is not great um you know there's something that ha
