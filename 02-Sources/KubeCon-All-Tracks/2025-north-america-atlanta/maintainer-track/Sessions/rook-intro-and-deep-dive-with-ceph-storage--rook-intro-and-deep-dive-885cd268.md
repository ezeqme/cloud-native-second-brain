---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "Storage Data", "Community Governance"]
speakers: ["Blaine Gardner", "Benamar Mekhissi", "IBM"]
sched_url: https://kccncna2025.sched.com/event/27NnB/rook-intro-and-deep-dive-with-ceph-storage-blaine-gardner-benamar-mekhissi-ibm
youtube_search_url: https://www.youtube.com/results?search_query=Rook%3A+Intro+and+Deep+Dive+With+Ceph+Storage+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Rook: Intro and Deep Dive With Ceph Storage - Blaine Gardner & Benamar Mekhissi, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Storage Data]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Blaine Gardner, Benamar Mekhissi, IBM
- Schedule: https://kccncna2025.sched.com/event/27NnB/rook-intro-and-deep-dive-with-ceph-storage-blaine-gardner-benamar-mekhissi-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=Rook%3A+Intro+and+Deep+Dive+With+Ceph+Storage+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Rook: Intro and Deep Dive With Ceph Storage.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27NnB/rook-intro-and-deep-dive-with-ceph-storage-blaine-gardner-benamar-mekhissi-ibm
- YouTube search: https://www.youtube.com/results?search_query=Rook%3A+Intro+and+Deep+Dive+With+Ceph+Storage+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=LmL2wyMWTXo
- YouTube title: Rook: Intro and Deep Dive With Ceph - Satoru Takeuchi, Cybozu, Inc.
- Match score: 0.876
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/rook-intro-and-deep-dive-with-ceph-storage/LmL2wyMWTXo.txt
- Transcript chars: 19283
- Keywords: cluster, storage, create, resource, operator, demons, object, support, volume, access, custom, resources, created, bucket, please, stoages, region, second

### Resumo baseado na transcript

And uh welcome to welcome and uh uh thank you for joining this session. And my name is Satar Takuchi and I'm one of the maintainers of uh Rook and I'm uh working for a Japanese software company Cyos and my company has been running uh a lot uh look safe clusters in production for years. So uh it provides uh uh many kinds of uh storage systems and uh for example uh it consist of four storage uh types. So the next slide is the safe also support uh remote replications and safe uh itself uh only support uh only supposed to create uh distributed storage in one data center or one region but uh safe can uh safe can achieve the remote replication. So uh the essential essential components of the uh safe is uh it consists of uh three essential components uh od demons mon demons and uh manager demons. So I will explain the uh the uh purpose of the uh these demons one by one.

### Excerpt da transcript

Okay. And uh welcome to welcome and uh uh thank you for joining this session. And my name is Satar Takuchi and I'm one of the maintainers of uh Rook and I'm uh working for a Japanese software company Cyos and my company has been running uh a lot uh look safe clusters in production for years. So here is uh this session's agenda. The first part is about the introduction to look and safe and second part is a block and file system storage provided by LU and safe and the third part is about the our object storage and the next part is uh about the other features provided by Rook. So the uh last part is the uh project of health about r community. So let's start from the first part uh introduction to rrook and safe. Uh ro is an open source uh kubernetes operator to manage uh sec cluster. So uh it's very beneficial for uh both administrators and users for something and uh uh for administrators uh they can deploy and manage upgrade and upgrade our safe cluster by custom resources. So it's very important because uh safe is very difficult to use.

Yes. So by using Rook uh your operation cost has been uh can be reduced very much. Please believe me. Yes. So for users uh they can consume uh safe by P just creating uh PPC or OBC custom resources. So the uh most important part is uh users uh don't care the uh their stories uh comes from uh safe or not. uh what they need is uh just creating the PBC and OBC resources. So probably you don't uh doesn't know about the uh object OBC custom resources but uh I'll explain about uh this uh custom resource later. So SE is uh an all-in-one open-source distributed storage platform. So uh it provides uh uh many kinds of uh storage systems and uh for example uh it consist of four storage uh types. The first one is an RBD. It provides block storage and the second one is the safe quest. It's a large scale uh shared file system storage. It's mainly uh used by the HPC systems or something. So the third one is RGW. RGW is an uh S3 compatible object storage. So the last one is SE NFS and SE NFS is uh uh just used for exporting the part of SES and exporting the S3 object as NFS.

So the next slide is the safe also support uh remote replications and safe uh itself uh only support uh only supposed to create uh distributed storage in one data center or one region but uh safe can uh safe can achieve the remote replication. So let's assume that there are two regions uh A and B and there are uh two safe cluster for each regions. In this case for exam
