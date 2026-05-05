---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Unclassified"
themes: ["GitOps Delivery"]
speakers: ["Jerome Kuptz", "Ameen Radwan", "Intuit"]
sched_url: https://kccncna2022.sched.com/event/182FV/how-intuit-manages-cloud-resources-via-gitops-jerome-kuptz-ameen-radwan-intuit
youtube_search_url: https://www.youtube.com/results?search_query=How+Intuit+Manages+Cloud+Resources+Via+GitOps+CNCF+KubeCon+2022
slides: []
status: parsed
---

# How Intuit Manages Cloud Resources Via GitOps - Jerome Kuptz & Ameen Radwan, Intuit

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[GitOps Delivery]]
- País/cidade: United States / Detroit
- Speakers: Jerome Kuptz, Ameen Radwan, Intuit
- Schedule: https://kccncna2022.sched.com/event/182FV/how-intuit-manages-cloud-resources-via-gitops-jerome-kuptz-ameen-radwan-intuit
- Busca YouTube: https://www.youtube.com/results?search_query=How+Intuit+Manages+Cloud+Resources+Via+GitOps+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre How Intuit Manages Cloud Resources Via GitOps.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182FV/how-intuit-manages-cloud-resources-via-gitops-jerome-kuptz-ameen-radwan-intuit
- YouTube search: https://www.youtube.com/results?search_query=How+Intuit+Manages+Cloud+Resources+Via+GitOps+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=V6L-xOUdoRQ
- YouTube title: How Intuit Manages Cloud Resources Via GitOps - Jerome Kuptz & Ameen Radwan, Intuit
- Match score: 0.812
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/how-intuit-manages-cloud-resources-via-gitops/V6L-xOUdoRQ.txt
- Transcript chars: 29602
- Keywords: actually, whatever, little, deploy, jenkins, infrastructure, essentially, resources, operations, developer, anything, create, process, deployment, engineers, workflow, environment, specific

### Resumo baseado na transcript

uh if you haven't heard of Intuit just a little brief introduction about us uh you may know Turbo Tax MailChimp but we run services on kubernetes Modern SAS and we're removing billions of dollars through our systems as well as uh billions of machine predictions and such things uh every day amongst the five platforms into it that we have as teams of me and myself are from the development of uh productivity and experience this platform and here numbers you can see the scale of what we attend then we just stumbled into the kind of I think a problem many of you may have had working at larger companies and you end up with a large ec2 Fleet and that gets to be a bit painful to manage which about I think 2018 to around there led us to Containers which obviously led us to kubernetes and and scaling up on that so all our services are pretty much in kubernetes on containers now we don't really run as much in ec2 anymore and that was a

### Excerpt da transcript

uh if you haven't heard of Intuit just a little brief introduction about us uh you may know Turbo Tax MailChimp but we run services on kubernetes Modern SAS and we're removing billions of dollars through our systems as well as uh billions of machine predictions and such things uh every day amongst the five platforms into it that we have as teams of me and myself are from the development of uh productivity and experience this platform and here numbers you can see the scale of what we attend to on a daily basis for our engineers and into it and finally um into its vague in the open source Community we just we received the end user award uh in 2019 and you may have noticed in the keynote we got it again this year we're also very involved with many projects as contributors as well as maintainers and these are just some of them out there and quick agenda so we're gonna go over a little bit about our history what our landscape looks like at Intuit discuss a little bit about the problem and we'll go over a solution show you a demo and do a q a so with that go ahead and get started into it's been on this journey for quite a while uh back in about 2013.

uh we've got foreign so yeah okay we um we started very narrow we declare we're going to be all in the cloud so we were getting out of data centers at that time and we started with just a few applications few of our services and once we had success with those we decided about let's say 2017 or so dates are yours are a little hazy at times we shifted the scale so we we had such good success we're like we're going to push everyone now let's all go into the cloud so there's much broader adoption within the company so Engineers were creating all kinds of cloud resources AWS accounts what whatever they needed to do they were pretty free to to meet the needs of their services and applications and then we just stumbled into the kind of I think a problem many of you may have had working at larger companies and you end up with a large ec2 Fleet and that gets to be a bit painful to manage which about I think 2018 to around there led us to Containers which obviously led us to kubernetes and and scaling up on that so all our services are pretty much in kubernetes on containers now we don't really run as much in ec2 anymore and that was a modernization of our services now we've had great success with that uh we were still left with a lot of stuff in AWS to for lack of a better word so we've been going down this path of moderniz
