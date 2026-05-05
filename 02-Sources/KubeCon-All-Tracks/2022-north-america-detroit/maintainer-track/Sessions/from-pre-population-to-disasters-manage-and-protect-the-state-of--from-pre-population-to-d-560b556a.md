---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Michael Henriksen", "Red Hat"]
sched_url: https://kccncna2022.sched.com/event/182NU/from-pre-population-to-disasters-manage-and-protect-the-state-of-vms-michael-henriksen-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=From+Pre-Population+To+Disasters%3A+Manage+And+Protect+the+State+Of+VMs+CNCF+KubeCon+2022
slides: []
status: parsed
---

# From Pre-Population To Disasters: Manage And Protect the State Of VMs - Michael Henriksen, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Michael Henriksen, Red Hat
- Schedule: https://kccncna2022.sched.com/event/182NU/from-pre-population-to-disasters-manage-and-protect-the-state-of-vms-michael-henriksen-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=From+Pre-Population+To+Disasters%3A+Manage+And+Protect+the+State+Of+VMs+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre From Pre-Population To Disasters: Manage And Protect the State Of VMs.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182NU/from-pre-population-to-disasters-manage-and-protect-the-state-of-vms-michael-henriksen-red-hat
- YouTube search: https://www.youtube.com/results?search_query=From+Pre-Population+To+Disasters%3A+Manage+And+Protect+the+State+Of+VMs+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=dQ5r_Wxkc1o
- YouTube title: From Pre-Population To Disasters: Manage And Protect the State Of VMs - Michael Henriksen, Red Hat
- Match score: 0.92
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/from-pre-population-to-disasters-manage-and-protect-the-state-of-vms/dQ5r_Wxkc1o.txt
- Transcript chars: 20162
- Keywords: source, virtual, volume, basically, machine, snapshot, export, cubert, create, images, cluster, storage, persistent, registry, populator, machines, running, everything

### Resumo baseado na transcript

hi there my name is Michael Hendrickson I'm software engineer at red hat and I'm here at cubec con North America 2022 to present from pre-population to disasters manage and protect the state of cubert VMS okay this session is for people that want to learn more about cubt storage a lot of the guts and details there um maybe you've contributed to core in the past and you want to do some storage related work um maybe you're just interested in how it all comes together both great reasons IMG file on a file system so pretty simple I mean uh for the most part um I think file system PVCs are the most common and this is what will probably be the most common um storage configuration okay cubert also supports block devices can use the API okay and yeah Valero plugin is [Music] um Valero first of all is a very popular open source kubernetes backup migration tool um it will basically backup your uh resource configuration you know yourls to an object store it will also user you know since the external provisioner ignored the PVC our controller is now responsible for binding it back up so that's what happens in uh step six here okay so that's volume populator kind of um the new kind of Club you know kubernetes

### Excerpt da transcript

hi there my name is Michael Hendrickson I'm software engineer at red hat and I'm here at cubec con North America 2022 to present from pre-population to disasters manage and protect the state of cubert VMS okay this session is for people that want to learn more about cubt storage a lot of the guts and details there um maybe you've contributed to core in the past and you want to do some storage related work um maybe you're just interested in how it all comes together both great reasons um so this session we'll talk a little bit about General cubert storage architecture we'll dig deep into um a couple specific API flows and Integrations um not uh the complete set of flows that support but some new and important ones that we've been working on and lastly we'll uh talk about what's coming up uh what you should be excited about in the future and hopefully by the end of this presentation you'll be pumped and ready to make some real meaningful uh contributions to cubt storage okay cubt storage architecture okay so when I and as to describe cubert in a couple words I typically say cubt is VMS and containers on kubernetes and yes that is a mouthful and probably means nothing to 99.9% of the population but to tech people that could mean a lot since those are all kind of floated terms so I will limit the scope of of I think what is relevant to this uh presentation by VMS I mean KVM virtual machines uh and I also mean VMS with persistent discs so VMS you can start stop start back up again and it picks up where you left off by containers I mean basically nothing special here just that you know containers run processes and in this case they're running virtual machine processes a qmu process and lastly uh since this is on kubernetes we're going to be talking about pods um and kubernetes persistence implies persistent blly claims so we'll be talking about that okay so this is kind of the cubert storage architecture um on the right is a persistent volume claim with a single file called dis.

IMG that is a virtual machine dis image that is what qmu kbm virtual machines expect to boot from most of the time they can be given kernels or or there are other things but for cubt we for the most part you boot from a dis image so how does that plug into the rest of the architecture here so when you start the VM pod gets created a pod has a container that runs a ver launcher process for launcher communicates with livert livert starts qmu which is basically your VM and the VM uh boots
