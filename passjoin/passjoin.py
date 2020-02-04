from collections import defaultdict


class Passjoin(object):

    def __init__(self, words, max_distance, distance_function):
        """
        """
        self._max_distance = max_distance
        self._distance_function = distance_function
        self._inverted_index_by_length = self._build_inverted_index_by_length(words, max_distance)

    def _build_inverted_index_by_length(self, words, max_distance):
        """
        """
        inverted_index_by_length = defaultdict(lambda: defaultdict(set))

        for word in words:
            length = len(word)
            for key in self._generate_segments(word):
                inverted_index_by_length[length][key].add(word)

        return inverted_index_by_length

    def _candidates_word_length_range(self, word):
        """
        """
        word_length = len(word)
        return range(
            max(0, word_length - self._max_distance),
            word_length + self._max_distance + 1
        )

    def _compute_partitions(self, word_length):
        """
        Computes how to partition a word given a max distance threshold
        Returns a list of tuple (partition_index, partition_start_index, partition_length)
        """
        segments_number = self._max_distance + 1
        small_segments_length = word_length // segments_number
        large_segments_length = small_segments_length + 1

        large_segments_number = word_length - small_segments_length * segments_number
        small_segments_number = segments_number - large_segments_number

        small_partitions = [
            (i, i * small_segments_length, small_segments_length)
            for i in range(small_segments_number)
        ]

        offset = small_segments_number * small_segments_length

        large_partitions = [
            (small_segments_number + j, offset + j * large_segments_length, large_segments_length)
            for j in range(large_segments_number)
        ]

        return small_partitions + large_partitions

    def _generate_segments(self, word):
        """
        """
        return [
            (i, word[start:start + length])
            for i, start, length in self._compute_partitions(len(word))
        ]

    def _minimum_start_position(self, length_delta, segment_index, s, segment_position):
        """
        """
        start_left = segment_position - segment_index  # left-side perspective
        start_right = segment_position + length_delta - (self._max_distance - segment_index)  # right-side perspective
        start_lower = 0  # lower-bound
        
        return max(start_left, start_right, start_lower)

    def _maximum_start_position(self, length_delta, segment_index, s, segment_position, segment_length):
        """
        """
        end_left = segment_position + segment_index  # left-side perspective
        end_right = segment_position + length_delta + (self._max_distance - segment_index)  # right-side perspective
        end_upper = s - segment_length  # upper-bound
        
        return min(end_left, end_right, end_upper)

    def _substrings_selection(self, word, candidate_length, segment_index, segment_position, segment_length):
        """
        """
        word_length = len(word)

        length_delta = word_length - candidate_length

        min_start_position = self._minimum_start_position(
            length_delta, segment_index, word_length, segment_position)

        max_start_position = self._maximum_start_position(
            length_delta, segment_index, word_length, segment_position, segment_length)

        return [
            word[ position : (position + segment_length) ]  
            for position in range(min_start_position, max_start_position + 1)
        ]

    def get_word_variations(self, word):
        """
        """
        variations = set()
        distance = self._distance_function
        max_distance = self._max_distance

        for candidate_length in self._candidates_word_length_range(word):
            inverted_index = self._inverted_index_by_length.get(candidate_length)

            if inverted_index is None:
                continue

            for partition_index, partition_start, partition_length in self._compute_partitions(candidate_length):
                for substring in self._substrings_selection(
                    word, candidate_length, partition_index, partition_start, partition_length
                ):
                    candidates = inverted_index.get((partition_index, substring), [])
                    for candidate in candidates:
                        if distance(word, candidate) <= max_distance:
                            variations.add(candidate)
        return variations

