---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Storage"
themes: ["Storage Data"]
speakers: ["Robert Vasek", "CERN"]
sched_url: https://kccnceu2022.sched.com/event/ytoh/your-manila-cephfs-share-backups-belong-to-s3-robert-vasek-cern
youtube_search_url: https://www.youtube.com/results?search_query=Your+Manila+CephFS+Share+Backups+Belong+to+S3+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Your Manila CephFS Share Backups Belong to S3 - Robert Vasek, CERN

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Storage]]
- Temas: [[Storage Data]]
- País/cidade: Spain / Valencia
- Speakers: Robert Vasek, CERN
- Schedule: https://kccnceu2022.sched.com/event/ytoh/your-manila-cephfs-share-backups-belong-to-s3-robert-vasek-cern
- Busca YouTube: https://www.youtube.com/results?search_query=Your+Manila+CephFS+Share+Backups+Belong+to+S3+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Your Manila CephFS Share Backups Belong to S3.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytoh/your-manila-cephfs-share-backups-belong-to-s3-robert-vasek-cern
- YouTube search: https://www.youtube.com/results?search_query=Your+Manila+CephFS+Share+Backups+Belong+to+S3+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=XfpP9pBTXfY
- YouTube title: Your Manila CephFS Share Backups Belong to S3 - Robert Vasek, CERN
- Match score: 0.913
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/your-manila-cephfs-share-backups-belong-to-s3/XfpP9pBTXfY.txt
- Transcript chars: 22051
- Keywords: backup, snapshot, volume, storage, backups, basically, application, around, valero, manual, workflow, snapshots, rustic, actually, support, drivers, memory, called

### Resumo baseado na transcript

all right hello and welcome to the talk about manual sffs share backups my name is robert and i work at cern as a junior fellow software engineer and i mainly focus on storage integration into container environments and their deployment etc so this is the agenda for the session first we'll have a look at what kind of storage we want to actually backup after that we'll briefly describe the individual components right after that we'll have a look uh exactly how we want to carry out the backups

### Excerpt da transcript

all right hello and welcome to the talk about manual sffs share backups my name is robert and i work at cern as a junior fellow software engineer and i mainly focus on storage integration into container environments and their deployment etc so this is the agenda for the session first we'll have a look at what kind of storage we want to actually backup after that we'll briefly describe the individual components right after that we'll have a look uh exactly how we want to carry out the backups what is the workflow we would like to follow uh after that uh we'll have a peek into the future that still needs to be done because as you'll see later on in the in the presentation there are still couple of blocker issues that we are facing and those need to be resolved first so i really take this whole talk more as a project update rather than a showcase of a final ready-to-use product and in the end we will uh conclude with the summary so quickly about cern itself it's the european organization for nuclear research it's located in geneva switzerland at the swiss french border it was founded in 1954 and its main mission is fundamental science which means it's trying to answer such questions as what is the 96 percent of the universe made of for this dark matter dark energy what was the state of matter just after the big bang and a lot more questions of this kind to try to answer those questions cern has built these very large machines called particle accelerators the one you can see on the photo here is the largest of its kind it's called lhc it's of a circular shape 27 kilometers in circumference and it's placed in a tunnel 100 meters below ground and in this in this tunnel there are two beams of protons being traveling uh in opposite directions and being accelerated uh very close to the speed of light and they are made to be collided with one another at uh at another kind of huge machines this is this one is called a detector that is then able to monitor the aftermath of the collision uh and this is basically what the physicists then study and analyze at cern those detectors generate huge amounts of data and even after all the filtering is done it's still tens of petabytes per year that needs to be stored and analyzed and for that we have we are running private cloud based on openstack this is a pretty recent screenshot of our graphone dashboard you can see we have around 460 000 physical cores 87 000 vms running on almost 58 000 hypervisors we are also running arou
