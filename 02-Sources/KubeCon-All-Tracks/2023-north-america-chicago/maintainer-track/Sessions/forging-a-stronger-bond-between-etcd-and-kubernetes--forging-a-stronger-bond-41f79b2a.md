---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Maintainer Track"
themes: ["AI ML", "Storage Data", "Kubernetes Core", "Community Governance"]
speakers: ["Marek Siarkowicz", "Wenjia Zhang", "Google", "James Blair", "Red Hat"]
sched_url: https://kccncna2023.sched.com/event/1R2rt/forging-a-stronger-bond-between-etcd-and-kubernetes-marek-siarkowicz-wenjia-zhang-google-james-blair-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Forging+a+Stronger+Bond+Between+Etcd+and+Kubernetes+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Forging a Stronger Bond Between Etcd and Kubernetes - Marek Siarkowicz & Wenjia Zhang, Google; James Blair, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Marek Siarkowicz, Wenjia Zhang, Google, James Blair, Red Hat
- Schedule: https://kccncna2023.sched.com/event/1R2rt/forging-a-stronger-bond-between-etcd-and-kubernetes-marek-siarkowicz-wenjia-zhang-google-james-blair-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Forging+a+Stronger+Bond+Between+Etcd+and+Kubernetes+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Forging a Stronger Bond Between Etcd and Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2rt/forging-a-stronger-bond-between-etcd-and-kubernetes-marek-siarkowicz-wenjia-zhang-google-james-blair-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Forging+a+Stronger+Bond+Between+Etcd+and+Kubernetes+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6JYgBJAjpNQ
- YouTube title: Forging a Stronger Bond Between Etcd and Kubernetes - Marek Siarkowicz, Wenjia Zhang & James Blair
- Match score: 0.788
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/forging-a-stronger-bond-between-etcd-and-kubernetes/6JYgBJAjpNQ.txt
- Transcript chars: 26478
- Keywords: contract, events, better, pretty, performance, testing, thanks, correctness, couple, actually, changes, interface, everyone, release, working, multiple, validate, member

### Resumo baseado na transcript

all right we should begin we got the sign um hello everyone uh Welcome to Our Sick SD sessions today and the topic is forging a stronger bound between s and kubernetes my name is wja from Google uh I am one of the sedd project maintainers and uh now I'm uh a co-chair of s SED and it's my pleasure to have uh Merrick and James to co-s speake with me um Merrick you want to Quick introduce to yourself sure uh hey I'm Mark shovi I'm I've been about the reconation loop but this is really just tip of the ice ber uh the the the most of the work to make uh kubernetes more more performant and scale better is done on the direct bottom uh on the the end uh and we' have seen a huge improvements be in performance because of this uh like there is two the two on the bottom watch uh watch list and consistent cash rats will really reimagine the performance that we can reach but uh it makes things uh

### Excerpt da transcript

all right we should begin we got the sign um hello everyone uh Welcome to Our Sick SD sessions today and the topic is forging a stronger bound between s and kubernetes my name is wja from Google uh I am one of the sedd project maintainers and uh now I'm uh a co-chair of s SED and it's my pleasure to have uh Merrick and James to co-s speake with me um Merrick you want to Quick introduce to yourself sure uh hey I'm Mark shovi I'm I've been ATD maintainer for last two years and with the creation of the sik I'm the tech lead for for it and very happy to have you here thanks mer hey team uh so my name is James bler I work at Red Hat uh and I'm a reviewer for Red CD along uh with a uh co-chair for um Sig CD as well with Wier that's me all right now let's get into our agenda uh today we'll first start with sharing a great news about SD all like we haven't mentioned s CD millions of times um and then uh Merrick will give us a deep dive about the API contract between kubernetes and S uh J followed by that um uh James will give us a detailed introduction of the new community model and the recent SD releases features announcements um we'll close this talk by providing a list of SD um opportunities or or uh activities here right um at K count and then we'll open up for questions so um it's been many years actually almost close to a decade now that SED had been playing a very critical role in kubernetes uh s is the data store for uh configuration data uh status data metadata for in kubernetes control plane so if we take a quick look at the brief history of kubernetes back in 2013 that's like actually a decade ago um the very first SD PR was committed to the SD repo and then very uh soon after that we had uh SD V 0.2 released at the time kubernetes is at 0.4 released and baby kubernetes adopted baby SD already then we released um version z uh 2.0 and then we rewrite the API release V3 and when time comes to 2018 in cucon Seattle on a ring day SD was officially accepted by cncf as a incubating project and there we were all getting together with the founder of s City uh maintainers of CD um to celebrate that moment and then 2 years after uh 2020 um SD moved to graduated level as a cncf project and yes SD is a pandemic graduate who can blame all the data inconsistency to that and then 3 years later um March this year Hong Kong and mer proposed a case of making SED a special interest group in kubernetes and um it took a little while to finalize all the details but we did it
