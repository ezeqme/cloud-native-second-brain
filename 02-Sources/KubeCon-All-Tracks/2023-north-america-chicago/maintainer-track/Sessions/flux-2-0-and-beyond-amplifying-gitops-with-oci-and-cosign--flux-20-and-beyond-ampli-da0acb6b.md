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
themes: ["AI ML", "GitOps Delivery", "Community Governance"]
speakers: ["Kingdon Barrett", "Sanskar Jaiswal", "Weaveworks"]
sched_url: https://kccncna2023.sched.com/event/1R2rK/flux-20-and-beyond-amplifying-gitops-with-oci-and-cosign-kingdon-barrett-sanskar-jaiswal-weaveworks
youtube_search_url: https://www.youtube.com/results?search_query=Flux+2.0+and+Beyond%3A+Amplifying+GitOps+with+OCI+and+Cosign+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Flux 2.0 and Beyond: Amplifying GitOps with OCI and Cosign - Kingdon Barrett & Sanskar Jaiswal, Weaveworks

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[GitOps Delivery]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Kingdon Barrett, Sanskar Jaiswal, Weaveworks
- Schedule: https://kccncna2023.sched.com/event/1R2rK/flux-20-and-beyond-amplifying-gitops-with-oci-and-cosign-kingdon-barrett-sanskar-jaiswal-weaveworks
- Busca YouTube: https://www.youtube.com/results?search_query=Flux+2.0+and+Beyond%3A+Amplifying+GitOps+with+OCI+and+Cosign+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Flux 2.0 and Beyond: Amplifying GitOps with OCI and Cosign.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2rK/flux-20-and-beyond-amplifying-gitops-with-oci-and-cosign-kingdon-barrett-sanskar-jaiswal-weaveworks
- YouTube search: https://www.youtube.com/results?search_query=Flux+2.0+and+Beyond%3A+Amplifying+GitOps+with+OCI+and+Cosign+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=pO2-Kgbkziw
- YouTube title: Flux 2.0 and Beyond: Amplifying GitOps with OCI and Cosign - Kingdon Barrett & Sanskar Jaiswal
- Match score: 0.861
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/flux-2-0-and-beyond-amplifying-gitops-with-oci-and-cosign/pO2-Kgbkziw.txt
- Transcript chars: 30792
- Keywords: flux, production, repository, release, staging, version, workflow, basically, github, verification, source, controller, charts, particular, registry, signature, repositories, container

### Resumo baseado na transcript

hi everyone um welcome to the flux Maino track uh today we're going to talk about how you can use flux to amplify your getop setup with oci cosign I'm sunar I'm a flux and Flagger meno I work at vok and my name is kingan I'm also a flux maintainer and I work at weave Works um this is a maintainer track so I'm going to assume most of you are familiar with flux for those of you who not let me do a quick inro flux is a been working fine uh but we have continuously run into issues by all of you is saying that Helm acts funky or there are certain problems it's sometimes it's too slow and from what we have seen majority of these issues can be tracked down DML just does not scale the approach of having to store all your charts or chart information in one file is just not a very scalable approach um there are several reasons for this uh first of all it's because it's a yam file and around for a long time but the problem with Providence files is that it's another file that you need to care about you need it's another file you need to manage and distribute um and these are not some theoretical predictions that we are making tml right which means that you don't have to spend as much as as much CPU in Ram uh as you were spending earlier which translates into cost efficiency you don't need to spend that much on English traffic which again translates into cost efficiency

### Excerpt da transcript

hi everyone um welcome to the flux Maino track uh today we're going to talk about how you can use flux to amplify your getop setup with oci cosign I'm sunar I'm a flux and Flagger meno I work at vok and my name is kingan I'm also a flux maintainer and I work at weave Works um this is a maintainer track so I'm going to assume most of you are familiar with flux for those of you who not let me do a quick inro flux is a CD tool which lets you do get offs for your communities clusters what that means is you can deploy your applications in a communities clust stor in a gitops fashion by storing them in a g repository or a hem repository u c uh it's a cncf graduated project uh we achieved graduation status last year uh we have multiple Integrations with terraform and AWS cloud formation and there is a free and open source UI you can use as well to view your flux resources and we are being used by companies like AWS and gitlab for their own giops offering as well as companies like orang and DT for their uh 5G deployments um so good news everyone flux finally has a g release uh yeah thank you [Applause] uh please what that means is that the core gitops apis that are the git repository API the customization API and the receiver API are all considered V1 which means that there are going to be no breaking changes so you're going to upgrade you can upgrade those apis whenever you want at your wish um flux if you don't know is built of multiple components and multiple apis um we like to evolve and iterate on these apis at our own fashion so that we can give the best uh experience to you users what that means is certain apis are still not considered GA which means they might have breaking changes for example Helm and oci Helm is considered close to ga we are working very hard on it It's tricky to get it right because Helm is Helm um so it's it's in the pipeline uh there's also oci repository which is a relatively new API uh which lets you fetch sources from oci Registries uh and then there is the image automation uh apis and then there's also the notification API which lets you do all sorts of alerting and uh updates to slacks and stuff okay so the basics of how with flux uh you have your Helm repository crd you have your three crds that each map to a particular artifact in the cluster the helm repository has an index.

yaml uh Helm chart is an instance of that chart so if you know about how Helm repositories worked historically that makes some sense it'll make more sens
