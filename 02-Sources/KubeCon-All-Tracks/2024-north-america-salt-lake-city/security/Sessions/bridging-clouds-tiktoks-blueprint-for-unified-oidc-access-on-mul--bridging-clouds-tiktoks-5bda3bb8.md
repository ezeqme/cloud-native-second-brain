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
themes: ["Security", "Kubernetes Core"]
speakers: ["Naveen Mogulla", "TikTok"]
sched_url: https://kccncna2024.sched.com/event/1i7lM/bridging-clouds-tiktoks-blueprint-for-unified-oidc-access-on-multi-cloud-kubernetes-naveen-mogulla-tiktok
youtube_search_url: https://www.youtube.com/results?search_query=Bridging+Clouds%3A+TikTok%E2%80%99s+Blueprint+for+Unified+OIDC+Access+on+Multi-Cloud+Kubernetes+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Bridging Clouds: TikTok’s Blueprint for Unified OIDC Access on Multi-Cloud Kubernetes - Naveen Mogulla, TikTok

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Naveen Mogulla, TikTok
- Schedule: https://kccncna2024.sched.com/event/1i7lM/bridging-clouds-tiktoks-blueprint-for-unified-oidc-access-on-multi-cloud-kubernetes-naveen-mogulla-tiktok
- Busca YouTube: https://www.youtube.com/results?search_query=Bridging+Clouds%3A+TikTok%E2%80%99s+Blueprint+for+Unified+OIDC+Access+on+Multi-Cloud+Kubernetes+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Bridging Clouds: TikTok’s Blueprint for Unified OIDC Access on Multi-Cloud Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7lM/bridging-clouds-tiktoks-blueprint-for-unified-oidc-access-on-multi-cloud-kubernetes-naveen-mogulla-tiktok
- YouTube search: https://www.youtube.com/results?search_query=Bridging+Clouds%3A+TikTok%E2%80%99s+Blueprint+for+Unified+OIDC+Access+on+Multi-Cloud+Kubernetes+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3flO98UANDU
- YouTube title: Bridging Clouds: TikTok’s Blueprint for Unified OIDC Access on Multi-Cloud Kubernetes - N. Mogulla
- Match score: 1.023
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/bridging-clouds-tiktoks-blueprint-for-unified-oidc-access-on-multi-clo/3flO98UANDU.txt
- Transcript chars: 31279
- Keywords: cluster, server, authorization, basically, request, whatever, access, provider, clusters, specific, identity, session, information, headers, management, pretty, groups, impersonation

### Resumo baseado na transcript

for coming my name is naven nain Mula I'm a tech lead with Tik Tok and I'm here to present bridging clouds Tik tok's blueprint for unified oadc access management on multicloud kubernetes clusters let me let me introduce my team first I'm part of the edge platform team and we are responsible for all the infrastructure for Edge use cases that includes you know Tik Tok CDM live streaming realtime Communications Tik Tok FL Etc and we have a global presence with multiple different regions we have a uh you know API server config file and it takes care of you know all of this user SST validation out of box from the kubernetes from the namespace point of view we basically Ma you know do that as part of the namespace management whenever the CD then you'll see that you know the identity Service Parts are running uh in your work and notes so you can see you know log into the you know parts and you can see the logs Etc all all all good things there

### Excerpt da transcript

for coming my name is naven nain Mula I'm a tech lead with Tik Tok and I'm here to present bridging clouds Tik tok's blueprint for unified oadc access management on multicloud kubernetes clusters let me let me introduce my team first I'm part of the edge platform team and we are responsible for all the infrastructure for Edge use cases that includes you know Tik Tok CDM live streaming realtime Communications Tik Tok FL Etc and we have a global presence with multiple different regions we have a uh region in US EU as well as the rest of the world and we have around 250 plus uh cuberes clusters across the globe and as a platform team we provide features uh on top of kubernetes like you know access management secret management logs metrics traffic management and metadata management Etc um predominantly we are on Prem kubernetes clusters we start our journey with on Prem because of the sheer volume of data and network bandwidth we deal with uh otherwise it's going to be too expensive if you go 100% Cloud so that being said um I just said on Prem and how did we end it up multicloud correct so first I let me talk a little bit about how did we even end it up in cloud first and then we go into the multic cloud so the cloud um I think it's pretty standard reasons before the cloud um you know when everyone is doing on on Prem anytime you want to add um you know new service to your site or you were building a new site new uh data center it could take weeks months years sometimes based on the logistics you know or whatever uh which is not in your control but on the other side application teams are expecting faster ramp of times because you know Tik Tok is going exponentially people want to test some features in a specific countries in a specific regions and uh they want it in a faster ramp of times so as a platform team we started looking into obviously in Cloud but on day Zero itself we realized that it's not like we're going to go into Cloud into one single cloud provider but rather we're going to go into on day Zero itself as a multicloud that reason being a couple of reasons obviously mean easily it's because of the business decisions or business requirements for example some of you may know you know Tik Tok and Oracle has some uh you know relationship and anything in us it's all in oci uh data center so that basically means that any us data you know uh kubernetes clusters it's going to be in oci but we also have similar um you know uh relationships with uh gcp and
