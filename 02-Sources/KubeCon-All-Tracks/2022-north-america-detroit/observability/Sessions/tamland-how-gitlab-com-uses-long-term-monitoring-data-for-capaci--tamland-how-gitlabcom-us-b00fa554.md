---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Observability"
themes: ["AI ML", "Observability", "Storage Data", "SRE Reliability"]
speakers: ["Andrew Newdigate", "GitLab", "Inc."]
sched_url: https://kccncna2022.sched.com/event/182IY/tamland-how-gitlabcom-uses-long-term-monitoring-data-for-capacity-forecasting-andrew-newdigate-gitlab-inc
youtube_search_url: https://www.youtube.com/results?search_query=Tamland%3A+How+GitLab.Com+Uses+Long-Term+Monitoring+Data+For+Capacity+Forecasting.+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Tamland: How GitLab.Com Uses Long-Term Monitoring Data For Capacity Forecasting. - Andrew Newdigate, GitLab, Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Observability]]
- Temas: [[AI ML]], [[Observability]], [[Storage Data]], [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Andrew Newdigate, GitLab, Inc.
- Schedule: https://kccncna2022.sched.com/event/182IY/tamland-how-gitlabcom-uses-long-term-monitoring-data-for-capacity-forecasting-andrew-newdigate-gitlab-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Tamland%3A+How+GitLab.Com+Uses+Long-Term+Monitoring+Data+For+Capacity+Forecasting.+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Tamland: How GitLab.Com Uses Long-Term Monitoring Data For Capacity Forecasting..

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182IY/tamland-how-gitlabcom-uses-long-term-monitoring-data-for-capacity-forecasting-andrew-newdigate-gitlab-inc
- YouTube search: https://www.youtube.com/results?search_query=Tamland%3A+How+GitLab.Com+Uses+Long-Term+Monitoring+Data+For+Capacity+Forecasting.+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Aa5IT3PWLO0
- YouTube title: Tamland: How GitLab.Com Uses Long-Term Monitoring Data For Capacity Forecasting. - Andrew Newdigate
- Match score: 0.982
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/tamland-how-gitlab-com-uses-long-term-monitoring-data-for-capacity-for/Aa5IT3PWLO0.txt
- Transcript chars: 29344
- Keywords: capacity, utilization, resource, saturation, approach, planning, resources, forecasting, cluster, maximum, database, gitlab.com, postgres, process, generate, metrics, gitlab, single

### Resumo baseado na transcript

hi everybody I hope you're all having a great conference thank you for coming to my talk about Tam land or how goodlab.com uses long-term monitoring data for capacity forecasting my name is Andrew nudigatz I'm a distinguished engineer in the infrastructure departments at gitlab where I focus on gitlab.com let's start with a bit of a backstory this Story begins in mid 2021 gitlab.com experienced a series of S1 database incidents related to high resource utilization on our primary postgres cluster within the company concerns were raised about the

### Excerpt da transcript

hi everybody I hope you're all having a great conference thank you for coming to my talk about Tam land or how goodlab.com uses long-term monitoring data for capacity forecasting my name is Andrew nudigatz I'm a distinguished engineer in the infrastructure departments at gitlab where I focus on gitlab.com let's start with a bit of a backstory this Story begins in mid 2021 gitlab.com experienced a series of S1 database incidents related to high resource utilization on our primary postgres cluster within the company concerns were raised about the growth rate of gitlab.com and the ability of our primary database to support this growth if the database hit maximum capacity it might lead to further outages due to saturation issues vertically scaling the main postgres cluster was no longer an option it was generally agreed that the way forward would be to split up the main postgres database into more than one cluster since a large proportion of our database traffic is related to CI it was decided to move this feature to a second postgres cluster through a process we called functional decomposition this would be a complicated project spanning months the fact that we wanted to keep the application running while migrating a huge volume of data to a new cluster made it even more complex a plan was devised and a date set for the completion of the migration but valid concerns were raised about whether given the recent space of postgres incidents the primary database could continue to support the growth we expected to see until the functional decomposition project was delivered one option would be to bring the project delivery dates forward but doing so would add additional risk to the project forcing Corners to be cut and possibly leading to further instability it would be much better if we could confirm that the database would have sufficient capacity allowing us to stick to the original date giving the take that giving the team the space to carry out the migration with due caution we needed an accurate and data-driven assessment of the available capacity in our main postgres cluster using a new tool called tameland we were able to carry out a capacity review with timeland we analyzed all potential saturation points within the cluster and plotted their individual growth forecasts to predict which if any would hit saturation we found that if a few small changes were made in the short term we'd have enough Runway to support the delivery of the functional decomposition o
