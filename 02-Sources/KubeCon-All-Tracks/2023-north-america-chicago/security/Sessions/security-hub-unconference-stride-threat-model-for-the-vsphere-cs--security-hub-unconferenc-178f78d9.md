---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Security"
themes: ["Security"]
speakers: []
sched_url: https://kccncna2023.sched.com/event/1UvYy/security-hub-unconference-stride-threat-model-for-the-vsphere-csi-driver
youtube_search_url: https://www.youtube.com/results?search_query=SECURITY+HUB+UNCONFERENCE%3A+STRIDE+threat+model+for+the+vSphere+CSI+Driver+CNCF+KubeCon+2023
slides: []
status: parsed
---

# SECURITY HUB UNCONFERENCE: STRIDE threat model for the vSphere CSI Driver

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: United States / Chicago
- Speakers: N/A
- Schedule: https://kccncna2023.sched.com/event/1UvYy/security-hub-unconference-stride-threat-model-for-the-vsphere-csi-driver
- Busca YouTube: https://www.youtube.com/results?search_query=SECURITY+HUB+UNCONFERENCE%3A+STRIDE+threat+model+for+the+vSphere+CSI+Driver+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre SECURITY HUB UNCONFERENCE: STRIDE threat model for the vSphere CSI Driver.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1UvYy/security-hub-unconference-stride-threat-model-for-the-vsphere-csi-driver
- YouTube search: https://www.youtube.com/results?search_query=SECURITY+HUB+UNCONFERENCE%3A+STRIDE+threat+model+for+the+vSphere+CSI+Driver+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1LIQFDc8CrQ
- YouTube title: SECURITY HUB UNCONFERENCE: STRIDE threat model for the vSphere CSI Driver
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/security-hub-unconference-stride-threat-model-for-the-vsphere-csi-driv/1LIQFDc8CrQ.txt
- Transcript chars: 27685
- Keywords: security, threat, diagrams, assessment, definitely, actors, question, driver, little, modeling, justin, looking, component, compromised, specific, excellent, pushker, effort

### Resumo baseado na transcript

hello everyone time to get started here so what are two things that go together well I'll start beans and toast for the British people in the audience uh can I get some other ideas on things that go together well very good one more example maybe fish and chips excellent all right so how about how about security and kubernetes okay so my name is all duberry I am the self assessment uh sub Project Lead in Sig security so super happy to be at this delightful little unconference

### Excerpt da transcript

hello everyone time to get started here so what are two things that go together well I'll start beans and toast for the British people in the audience uh can I get some other ideas on things that go together well very good one more example maybe fish and chips excellent all right so how about how about security and kubernetes okay so my name is all duberry I am the self assessment uh sub Project Lead in Sig security so super happy to be at this delightful little unconference session here uh so yeah I just wanted to pull up the git repo so like I said we're part of uh Sig security here so today what I wanted to do with this session o that looks very messy let's hit Refresh on that and see what happens um is to just go through uh the progress that we've made so far with the Vere CSI driver self assessment um so just to back up for a second for folks who may not be familiar with the self assessment sub project in Sig security we are the lightweight threat modeling uh sub project uh started by pushker um who is amazing thank you for all that you do and um yeah so to just really oh yes Justin yes that is very accurate and just for anyone who couldn't hear this is as of now separate but we are hoping to make it more related and more um a part of what's going on in tag security and has definitely been uh was originally an effort by pushker to bring the goodness of what's going on into tag security into kubernetes did I get that right pushker just going to add like Justin is absolutely right at least both the groups are not named six security anymore so that's a start uh and U you I think tax security has been way ahead and started with assessments Way Long back and this is relatively a very new sub project we've done one self assessment basically trying to adopt whatever we can from the good assessments we have done in the past and trying trying to utilize the huge number of contributors we have in kubernetes so that we can be self- sustaining at the same time having a link back to the Mothership in some ways to security tag and uh this is a good opportunity for all of us to kind of meet uh kind of vars where we are uh see if Allah needs any help and see where we can help her so that's that's more more to the context of where we are excellent thank you so yes high level uh I we we do need help I need help um it is this is definitely um you know a group effort here so what I wanted to do really quick is to just at a high level look at the data flow diagrams that w
