---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Sponsor Theater"
themes: ["AI ML"]
speakers: ["Tom Manville", "Michael Cade", "Kasten by Veeam"]
sched_url: https://kccnceu2021.sched.com/event/igUT/sponsored-session-securing-s3-backups-against-ransomware-tom-manville-michael-cade-kasten-by-veeam
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Session%3A+Securing+S3+Backups+Against+Ransomware+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Sponsored Session: Securing S3 Backups Against Ransomware - Tom Manville & Michael Cade, Kasten by Veeam

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Sponsor Theater]]
- Temas: [[AI ML]]
- País/cidade: Virtual / Virtual
- Speakers: Tom Manville, Michael Cade, Kasten by Veeam
- Schedule: https://kccnceu2021.sched.com/event/igUT/sponsored-session-securing-s3-backups-against-ransomware-tom-manville-michael-cade-kasten-by-veeam
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Session%3A+Securing+S3+Backups+Against+Ransomware+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Sponsored Session: Securing S3 Backups Against Ransomware.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/igUT/sponsored-session-securing-s3-backups-against-ransomware-tom-manville-michael-cade-kasten-by-veeam
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Session%3A+Securing+S3+Backups+Against+Ransomware+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=S_A-xHBT13g
- YouTube title: Sponsored Session: Securing S3 Backups Against Ransomware - Tom Manville & Michael Cade, Kasten
- Match score: 0.852
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/sponsored-session-securing-s3-backups-against-ransomware/S_A-xHBT13g.txt
- Transcript chars: 16032
- Keywords: object, backup, backups, ransomware, retention, version, around, immutable, access, bucket, storage, cannot, period, platform, whether, within, security, environment

### Resumo baseado na transcript

[Music] thank you for joining our session on securing s3 backups against ransomware so as we get into this just a bit of an introduction so i'm michael cade i'm a senior technologist here at cast and by veeam and i'm joined by tom hi everyone my name is tom manville i'm director of engineering here at cast and by veeam and i was on the founding team at caston awesome tom's going to be giving the good news later on before that i have to put in some of

### Excerpt da transcript

[Music] thank you for joining our session on securing s3 backups against ransomware so as we get into this just a bit of an introduction so i'm michael cade i'm a senior technologist here at cast and by veeam and i'm joined by tom hi everyone my name is tom manville i'm director of engineering here at cast and by veeam and i was on the founding team at caston awesome tom's going to be giving the good news later on before that i have to put in some of the doom and gloom around well just the reality of why do we need to protect our data against things like ransomware so i'll get into the the bad bits first and then tom can tom can bring it home later on so the first thing that we want to touch on is well what is the need for a mutual backups and as much as we're talking around specifically around kubernetes clusters and kubernetes data the actual premise here actually resides in any any other platform so whether it's virtualization whether it's cloud-based ios workloads whether it's on-premises physical machines they all of these player play a a reason why we we need and we should be considering that mutability within our within our backup chains or off-site copies as well so just to quickly run through what these look like accidental deletion and i'm going to come through and put some of these into specific use cases later on like we know people make mistakes and if we look at if we were going to look at um the analysts who are constantly speaking to to you guys and understanding what happens from a failure scenario point of view accidental deletion is always in the top three things that are causing for data loss then you've got policy gaps in terms of well i thought you were backing this up i thought we were backing that up and there's that confusion gap around what is being what is actually being protected and what actually is being um backed up to a different location for to prevent those failure scenarios or not being able to recover from those failure scenarios and then probably more and definitely over the last 12 months is around security so both internal security threats there's a growing number of insider malicious activity going on i'm going to touch on this a little bit later as well as well as that everyday news wire coming down around external security threats and namely around ransomware and that's really the point where a ransomware attack is going to try and get into your system it's going to try and encrypt encrypt your data at a very 101 l
