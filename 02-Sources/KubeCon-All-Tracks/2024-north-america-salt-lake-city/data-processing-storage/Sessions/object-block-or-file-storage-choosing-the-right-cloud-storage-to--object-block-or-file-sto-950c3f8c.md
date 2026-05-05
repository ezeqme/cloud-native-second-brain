---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Data Processing + Storage"
themes: ["Storage Data", "Kubernetes Core"]
speakers: ["Mitch Becker", "Tom McDonald", "Amazon Web Services (AWS)"]
sched_url: https://kccncna2024.sched.com/event/1i7r1/object-block-or-file-storage-choosing-the-right-cloud-storage-to-integrate-into-kubernetes-mitch-becker-tom-mcdonald-amazon-web-services-aws
youtube_search_url: https://www.youtube.com/results?search_query=Object%2C+Block%2C+or+File+Storage%3F+Choosing+the+Right+Cloud+Storage+to+Integrate+Into+Kubernetes+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Object, Block, or File Storage? Choosing the Right Cloud Storage to Integrate Into Kubernetes - Mitch Becker & Tom McDonald, Amazon Web Services (AWS)

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Mitch Becker, Tom McDonald, Amazon Web Services (AWS)
- Schedule: https://kccncna2024.sched.com/event/1i7r1/object-block-or-file-storage-choosing-the-right-cloud-storage-to-integrate-into-kubernetes-mitch-becker-tom-mcdonald-amazon-web-services-aws
- Busca YouTube: https://www.youtube.com/results?search_query=Object%2C+Block%2C+or+File+Storage%3F+Choosing+the+Right+Cloud+Storage+to+Integrate+Into+Kubernetes+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Object, Block, or File Storage? Choosing the Right Cloud Storage to Integrate Into Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7r1/object-block-or-file-storage-choosing-the-right-cloud-storage-to-integrate-into-kubernetes-mitch-becker-tom-mcdonald-amazon-web-services-aws
- YouTube search: https://www.youtube.com/results?search_query=Object%2C+Block%2C+or+File+Storage%3F+Choosing+the+Right+Cloud+Storage+to+Integrate+Into+Kubernetes+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=QQgmaHqKRyY
- YouTube title: Object, Block, or File Storage? Choosing the Right Cloud Storage to Integr... M. Becker, T. McDonald
- Match score: 0.931
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/object-block-or-file-storage-choosing-the-right-cloud-storage-to-integ/QQgmaHqKRyY.txt
- Transcript chars: 25258
- Keywords: storage, object, applications, persistent, workloads, cost, application, actually, access, performance, developers, choose, stateful, cluster, important, available, talking, volumes

### Resumo baseado na transcript

good afternoon everybody thanks for hanging in there it's Friday afternoon last day of cubec con you've made it this far you just need to hang with us for another half hour or so and uh we look forward to meeting with you my name is Mitch Becker I'm a senior storage specialist with Amazon web services I'm Tom McDonald uh I'm an old Unix and Linux administrator I am now a storage solutions architect at AWS that's a big title yeah I'm not too much into titles well thanks

### Excerpt da transcript

good afternoon everybody thanks for hanging in there it's Friday afternoon last day of cubec con you've made it this far you just need to hang with us for another half hour or so and uh we look forward to meeting with you my name is Mitch Becker I'm a senior storage specialist with Amazon web services I'm Tom McDonald uh I'm an old Unix and Linux administrator I am now a storage solutions architect at AWS that's a big title yeah I'm not too much into titles well thanks for joining us today Tom yeah we're going to talk about a number of things today uh there the agenda straightforward and self-explanatory but I I had a question for you what is the c yo a is that like cover your Argo cover your Apache cover your something I shouldn't say Choose Your Own Adventure and we've got a slide on it in a bit okay outstanding well discovering what kind of storage to you use very much is an adventure so I can see why you chose that title I want to do a quick level set on expectations so we got about a half an hour and if you don't know a lot about storage um You probably won't come out of here in that short time frame knowing exactly what to do but I'm confident that in the time frame we'll give you enough guidance well you'll have a flashlight in your hand and you can find the answers so with that there's just not a quick fix to storage but you're going to learn a lot today well you know who we are we've already covered that but I'm kind of curious just a quick query um in terms of incu kubernetes how many of you are using block storage which is the preceding presentation okay fair number how many of you are using um object a little bit of big number and how many are using let's say file storage in kubernetes okay kind of an even spread uh perhaps a database or data warehouse okay A bit less but a fair amount excellent um and maybe something else that I didn't cover okay that's good so there's no such thing as status and you might not want to be the ostrich with your head in the ground CU all applications store State somewhere because you might choose to be the ostrich with these cool pink sunglasses because your future is so bright you need to wear sunglasses and and if you do Tom will buy you the sunglasses I'm not buying pink I'll buy them orange maybe orange yeah you're into Orange today I see that's very flashy so I got the idea for this slide actually I was listening to uh Alex cherop he's the uh one of the chair for the storage technical Advisory Group for the
