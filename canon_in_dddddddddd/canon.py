import argparse
import partitura
import copy

parser = argparse.ArgumentParser()
parser.add_argument('in', help="Input musicxml file")
parser.add_argument('out', help="Destination file")
parser.add_argument('--note', help='Change the note to replicate')
args = parser.parse_args()

score = partitura.load_musicxml(getattr(args, "in"))

to_purge = []
added_notes = []

for note in score.timeline.iter_all(partitura.score.Note, include_subclasses=True):
    if note.step == "D" and note not in added_notes and note.duration > 1:
        containing_timepoint = next(iter([point for point in score.timeline.points if note in point.starting_objects[partitura.score.Note]]))
        for i in range(0, note.duration):
            new_d = copy.copy(note)
            new_d._sym_dur = None
            new_d.start = score.timeline.get_or_add_point(note.start.t + i)
            new_d.end = score.timeline.get_or_add_point(new_d.start.t + 1)
            score.timeline.add(new_d, containing_timepoint.t + i, containing_timepoint.t + i + 1)
            to_purge.append(note)
            added_notes.append(new_d)

for note in to_purge:
    score.timeline.remove(note)

f = open(args.out, "wb")
partitura.save_musicxml(score, f)
f.close()
