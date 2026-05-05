---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Unclassified"
themes: ["AI ML", "Storage Data", "Kubernetes Core"]
speakers: ["Conor Nolan", "Richard Kovacs", "Akamai"]
sched_url: https://kccnceu2024.sched.com/event/1YeSq/object-storage-on-kubernetes-completed-it-with-provider-ceph-conor-nolan-richard-kovacs-akamai
youtube_search_url: https://www.youtube.com/results?search_query=Object+Storage+on+Kubernetes%3F+Completed+It+with+Provider+Ceph.+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Object Storage on Kubernetes? Completed It with Provider Ceph. - Conor Nolan & Richard Kovacs, Akamai

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Conor Nolan, Richard Kovacs, Akamai
- Schedule: https://kccnceu2024.sched.com/event/1YeSq/object-storage-on-kubernetes-completed-it-with-provider-ceph-conor-nolan-richard-kovacs-akamai
- Busca YouTube: https://www.youtube.com/results?search_query=Object+Storage+on+Kubernetes%3F+Completed+It+with+Provider+Ceph.+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Object Storage on Kubernetes? Completed It with Provider Ceph..

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeSq/object-storage-on-kubernetes-completed-it-with-provider-ceph-conor-nolan-richard-kovacs-akamai
- YouTube search: https://www.youtube.com/results?search_query=Object+Storage+on+Kubernetes%3F+Completed+It+with+Provider+Ceph.+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=tZhDQpmzaS0
- YouTube title: Object Storage on Kubernetes? Completed It with Provider Ceph. - Conor Nolan & Richard Kovacs
- Match score: 0.896
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/object-storage-on-kubernetes-completed-it-with-provider-ceph/tZhDQpmzaS0.txt
- Transcript chars: 28334
- Keywords: bucket, crossplane, provider, resource, server, cluster, custom, buckets, reconcile, memory, resources, conditions, booket, everything, performance, created, itself, operator

### Resumo baseado na transcript

my name is Connor Nolan I'm a senior software engineer akami and I'm joined by my colleague rehard he's going to speak a little bit later hello everyone and uh we're here to talk about uh provider SEF which is an open source crossplane provider that we've been developing over the last year or so uh and we use it to manage uh S3 buckets in SEF clusters from kubernetes uh so I'll go through a little bit of the agenda kind of what we have in store today um you can see that the etcd is is sleeping all threads are waiting for Io and once etcd is dead the next component would be the API manager after a while it would dead and when API manager is down the kubernetes controller manager goes

### Excerpt da transcript

my name is Connor Nolan I'm a senior software engineer akami and I'm joined by my colleague rehard he's going to speak a little bit later hello everyone and uh we're here to talk about uh provider SEF which is an open source crossplane provider that we've been developing over the last year or so uh and we use it to manage uh S3 buckets in SEF clusters from kubernetes uh so I'll go through a little bit of the agenda kind of what we have in store today um I'm going to give a bit of background kind of how we ended up here uh the challenge that we faced and um then how we over overcame that some of the specific requirements and how that led us to uh cross plane a little bit about crossplane I won't go into too much detail on it um but kind of how it works for us and how it's a kind of the perfect solution for us um so then I'll get into provider St itself give a little bit of an overview um some of the features how it works that kind of thing then rehard is going to take over give us a demo and uh get into kind of a discussion then on uh scalability and performance that kind of thing then we'll wrap up with a Q&A and uh head for the airport okay so uh like I said a little bit of background rehard and I both uh previously worked at a company called andat which was a London based uh kubernetes startup uh it was originally called storage OS later rebranded as on dash you might recognize the logos from previous cubec cons um but as well what what we did there was we offered a kubernetes native uh block storage solution and as part of delivering that we uh maintained a bunch of different kubernetes peripherals so we had a cube plugin bunch of Helm charts obviously a CSI driver and then we had probably half a dozen or so kubernetes operators uh all of which were like CU Builder based um so we would be kind of intimately familiar with that whole branch of the kubernetes ecosystem the operator pattern all that and that kind of uh I suppose informed our decision making going forward on this um so then about a year ago I think actually about a year ago this week I'm not sure the exact dates but we were acquired by akami and then that led us to uh a new challenge which kind of combined our history and knowledge of uh kubernetes and storage so the specifics of that challenge were uh we need to be able to manage uh S3 buckets across Ross multiple distributed SE clusters and we need to be able to do that from within a single kubernetes cluster so basically we're going to ha
