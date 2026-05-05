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
themes: ["GitOps Delivery"]
speakers: ["Yudi Andrean Phanama", "Giri Kuncoro", "GoTo Financial"]
sched_url: https://kccncna2023.sched.com/event/1R2po/goto-financials-story-towards-10k-argocd-apps-to-support-billions-of-transactions-yudi-andrean-phanama-giri-kuncoro-goto-financial
youtube_search_url: https://www.youtube.com/results?search_query=GoTo+Financial%E2%80%99s+Story%3A+Towards+10k+ArgoCD+Apps+to+Support+Billions+of+%24+Transactions+CNCF+KubeCon+2023
slides: []
status: parsed
---

# GoTo Financial’s Story: Towards 10k ArgoCD Apps to Support Billions of $ Transactions - Yudi Andrean Phanama & Giri Kuncoro, GoTo Financial

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[SDLC]]
- Temas: [[GitOps Delivery]]
- País/cidade: United States / Chicago
- Speakers: Yudi Andrean Phanama, Giri Kuncoro, GoTo Financial
- Schedule: https://kccncna2023.sched.com/event/1R2po/goto-financials-story-towards-10k-argocd-apps-to-support-billions-of-transactions-yudi-andrean-phanama-giri-kuncoro-goto-financial
- Busca YouTube: https://www.youtube.com/results?search_query=GoTo+Financial%E2%80%99s+Story%3A+Towards+10k+ArgoCD+Apps+to+Support+Billions+of+%24+Transactions+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre GoTo Financial’s Story: Towards 10k ArgoCD Apps to Support Billions of $ Transactions.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2po/goto-financials-story-towards-10k-argocd-apps-to-support-billions-of-transactions-yudi-andrean-phanama-giri-kuncoro-goto-financial
- YouTube search: https://www.youtube.com/results?search_query=GoTo+Financial%E2%80%99s+Story%3A+Towards+10k+ArgoCD+Apps+to+Support+Billions+of+%24+Transactions+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=qoN9Exm7Ue4
- YouTube title: GoTo Financial’s Story: Towards 10k ArgoCD Apps to Support Bi... Yudi Andrean Phanama & Giri Kuncoro
- Match score: 0.839
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/goto-financials-story-towards-10k-argocd-apps-to-support-billions-of-t/qoN9Exm7Ue4.txt
- Transcript chars: 27270
- Keywords: argo, application, controller, cluster, server, instance, platform, clusters, applications, centralized, actually, objects, components, request, fields, manifest, maintain, across

### Resumo baseado na transcript

hello folks Welcome to our talk today we'll be sharing our story in running 10,000 Argos applications and sharing our journey in tuning the performance of our Argus CID instance my name is giri and this is my colag Udi both of us are infra Engineers from go goto Financial goto Financial is a financial arm part of financial arm part of uh goto group the leading digital ecosystem in Indonesia we provide various service offerings from ride hailing service using motorcycle food delivery service package delivery service e-commerce platform

### Excerpt da transcript

hello folks Welcome to our talk today we'll be sharing our story in running 10,000 Argos applications and sharing our journey in tuning the performance of our Argus CID instance my name is giri and this is my colag Udi both of us are infra Engineers from go goto Financial goto Financial is a financial arm part of financial arm part of uh goto group the leading digital ecosystem in Indonesia we provide various service offerings from ride hailing service using motorcycle food delivery service package delivery service e-commerce platform and many other services to start off um I'm going to give you a brief uh overview of the state of current of our kubernetes and Argo City we maintain around 50 kubernetes clusters across NWS gcp and private data center in Singapore and Indonesia region this consists of 700 compute notes 15,000 CPUs 120 TB memories and more than 30,000 pods this Argo City dashboard uh snapshot we took uh two weeks back there's an interesting story behind this snapshot when we were preparing for cubec con proposal this St few months back we were at uh 7,000 aru CD apps and looking at the growth rate of our agdf app creation we predicted today we would reach above 10,000 that's why the title 10,000 arusd apps and today we made it it's now uh 11,000 arusd applications these 11,000 applications are coming from 6,000 repositories across 60 different projects Argo City watch uh more than 30 380,000 total objects on our largest cluster we run 2,000 applications and Argo CD watch over 40,000 objects we adopted a simple centralized Argo CD instance model which is technically a push model or some of you refer it as Hub and spoke model in hubit Spoke model we have management cluster where we run our single Argo CD instance this Argo CD instance reads a common git repository sorry git uh git providers and then using this uh the the the manifest stored in G repository the aroid instance push objects across all the Clusters that get registered under aroid instance there's couple of benefits with this simple centralized Argus cidd instance it's very easy to maintain and upgrade because we only need to upgrade one argocd instance regularly it's very easy to integrate with our automation at platform internally we maintain a developer platform that is tightly uh related to argd instance so maintaining only one argd version makes it very simple to write our integration logic in the platform it's very easy to manage centralized arback because everything is in one
