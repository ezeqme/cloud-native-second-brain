---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Community Governance"]
speakers: ["Alex Xu", "Wang Yan", "Steven Zou", "Deng Qian", "Ziming Zhang", "VMware"]
sched_url: https://kccncna2021.sched.com/event/lV7u/harbor-enterprise-cloud-native-artifact-registry-alex-xu-wang-yan-steven-zou-deng-qian-ziming-zhang-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Harbor+-+Enterprise+Cloud+Native+Artifact+Registry+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Harbor - Enterprise Cloud Native Artifact Registry - Alex Xu, Wang Yan, Steven Zou, Deng Qian & Ziming Zhang, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Alex Xu, Wang Yan, Steven Zou, Deng Qian, Ziming Zhang, VMware
- Schedule: https://kccncna2021.sched.com/event/lV7u/harbor-enterprise-cloud-native-artifact-registry-alex-xu-wang-yan-steven-zou-deng-qian-ziming-zhang-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Harbor+-+Enterprise+Cloud+Native+Artifact+Registry+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Harbor - Enterprise Cloud Native Artifact Registry.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV7u/harbor-enterprise-cloud-native-artifact-registry-alex-xu-wang-yan-steven-zou-deng-qian-ziming-zhang-vmware
- YouTube search: https://www.youtube.com/results?search_query=Harbor+-+Enterprise+Cloud+Native+Artifact+Registry+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=FU7A6WXoCt0
- YouTube title: Harbor - Enterprise Cloud Native Artifact Registry - Daniel Jiang & Yan Wang, VMware
- Match score: 0.848
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/harbor-enterprise-cloud-native-artifact-registry/FU7A6WXoCt0.txt
- Transcript chars: 17755
- Keywords: hardware, harbor, rubber, version, account, provide, projects, secret, created, features, artifacts, working, harvard, information, storage, release, prefix, operator

### Resumo baseado na transcript

um let's get started hey everyone uh thanks for tuning in i'm very happy to be here to talk to you guys uh about project harbor uh i'm daniel i'm a software engineer from vmware i'm also a maintainer of harvard today with me is my co-presenter yan and you want to say hi to the audience hi i'm ian i'm also a hardware maintenance i work with daniel inhabiting okay thank you now first because we only have one maintainer section in this coupon i'll start by giving an

### Excerpt da transcript

um let's get started hey everyone uh thanks for tuning in i'm very happy to be here to talk to you guys uh about project harbor uh i'm daniel i'm a software engineer from vmware i'm also a maintainer of harvard today with me is my co-presenter yan and you want to say hi to the audience hi i'm ian i'm also a hardware maintenance i work with daniel inhabiting okay thank you now first because we only have one maintainer section in this coupon i'll start by giving an introduction to this product uh for those who are new harbor is an on-prem cloud native registry we started the project by adding features around the darker distribution to provide a better experience for managing docker images and later with the growth of the user base more management features were added then in another in a major upgrade we expand the scope of hardware from managing only container images to all the oci uh cloud native artifacts and with a great support from the community harvard has officially become a graduated project in cncf since last year which is really exciting let's take a look at the key features harbour provide the access control for the artifacts the artifacts are isolated within projects a user is granted the permission to access the artifacts by being added as members to a project project is also a unit of management admin can assign different policies to products for example there's an immutability policy to prevent artifacts from being overridden and quota policy to limit the storage usage of a product and the retention policy which can help you remove the stale artifacts so you don't use all the quota too fast however also provides powerful features to help you distribute the artifacts across different uh registries in the cloud you can use the replication to transfer artifacts to or from different registries and also the proxy cache which helps you configure a project as a cache so the client can get content from a remote registry synchronously security has also i mean it has always been a big concern for enterprise users to help users deal with that helper harbor has a flexible scanning framework by implementing the adapters scanners can be plugged into hover and admin can trigger the scanner to scan the image or artifact and view the cvs in the scan report hover also integrates with notary to support image signing to enhance security of the workload admin can set the policies in harbor to prevent image with you know high cve scores or invalid signature from be
